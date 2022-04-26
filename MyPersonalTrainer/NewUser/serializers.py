from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import Account
from allauth.account.admin import EmailAddress

User = get_user_model()


class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        is_verified = EmailAddress.objects.filter(
            email=email, verified=True).exists()
        check_email = User.objects.filter(email=email).exists()

        if email and password:
            if check_email:
                if is_verified:
                    user = authenticate(request=self.context.get('request'),
                                        email=email, password=password)
                if not is_verified:
                    msg = {
                        'detail': 'We have Send Verification mail,Please check your inbox and verifiy your email'}
                    raise serializers.ValidationError(
                        msg, code='authorization')

            if not user:
                msg = {'detail': 'Unable to log in with provided credentials.'}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "Email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'username']
