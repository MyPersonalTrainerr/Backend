from django.shortcuts import render
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render (request,'home/index.html')



# Create your views here.
def signUp(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    # return render(request,'home/index.html',{'form':form})