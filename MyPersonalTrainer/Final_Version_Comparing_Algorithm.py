import json
import math
import os
import time
import matplotlib.pyplot as plt
from natsort import natsorted
import numpy as np


# def Existed_JsonFiles():
#     path_to_json = '/home/awatef/GP/MyPersonalTrainer'
#     json_files = [pos_json for pos_json in os.listdir(
#         path_to_json) if pos_json.endswith('.json')]
#     Sorted_List = natsorted(json_files)
#     return (Sorted_List)


# list_of_jsons = Existed_JsonFiles()

Shoulder_Y_Positions=[]
Hip_Y_Positions=[]
Knee_Y_Positions=[]
Ankle_Y_Positions=[]

Shoulder_X_Positions=[]
Hip_X_Positions=[]
Knee_X_Positions=[]

Knee_X_Positions_25=[]
Knee_X_Positions_26=[]

Ankle_X_Positions=[]
Toes_X_Positions=[]


Index_Of_KeyPoints = []

# shoulder,hip,knee,foot,toes
Even_KeyPoints = ['12', '24', '26', '28', '30', '32']
Odd_KeyPoints = ['11', '23', '25', '27', '29', '31']

Knee_WRT_Toes_25_26 = []
Knee_Notes=[]
Hip_WRT_Knee_23_24 = []
Hip_Notes=[]

Direction = "right"
New_Hip_Y_Positions = []
Indecies_Of_Deleted_Values = []
Max_Y_Hip=[]
# New_Max_Y_Hip=[]
Max_index = []
Min_Y_Hip=[]
# New_Min_Y_Hip=[]
Min_index = []

Max_Hip_Knee_Angles=[]
Min_Hip_Knee_Angles=[]
KneeAngle_Notes=[]
Min_Knee_Angle_Status=[]
Status_of_Max_Hip_Knee_Angles=[]

Max_Back_Angle=[]
Min_Back_Angle=[]
Min_Back_Angle_Status=[]
Max_Back_Angle_Status=[]
MinBackAngle_Notes=[]
MaxBackAngle_Notes=[]

original_indecies_max=[]
original_indecies_min=[]

def Knee_Angle(index):
    vector_Hip_Knee=[Hip_X_Positions[index]-Knee_X_Positions[index],Hip_Y_Positions[index]-Knee_Y_Positions[index]]
    vector_Knee_Ankle=[Knee_X_Positions[index]-Ankle_X_Positions[index],Knee_Y_Positions[index]-Ankle_Y_Positions[index]]
    magnitudeA=math.sqrt(vector_Hip_Knee[0]**2+vector_Hip_Knee[1]**2)
    magnitudeB=math.sqrt(vector_Knee_Ankle[0]**2+vector_Knee_Ankle[1]**2)
    dotProduct=(vector_Hip_Knee[0]*vector_Knee_Ankle[0])+(vector_Hip_Knee[1]*vector_Knee_Ankle[1])
    cosTheta=(dotProduct)/(magnitudeA*magnitudeB)
    theta=math.degrees(math.acos(cosTheta))
    knee_Angle=180-theta

    return knee_Angle

def Back_Angle(index):
    vector_Back=[Shoulder_X_Positions[index]-Hip_X_Positions[index],Shoulder_Y_Positions[index]-Hip_Y_Positions[index]]
    Y_Axis=[0,1]
    magnitudeA=math.sqrt(vector_Back[0]**2+vector_Back[1]**2)
    magnitudeB=math.sqrt(Y_Axis[0]**2+Y_Axis[1]**2)
    dotProduct=(vector_Back[0]*Y_Axis[0])+(vector_Back[1]*Y_Axis[1])
    cosTheta=(dotProduct)/(magnitudeA*magnitudeB)
    theta=math.degrees(math.acos(cosTheta))
    
    return theta



def Extract_Positions_Of_KeyPoints(jsonPath):
    with open(jsonPath, 'r') as jsonfile:
        Json_File = json.loads(jsonfile.read())

        if Json_File[0].get('32')[0] < Json_File[0].get('30')[0]:
            Index_Of_KeyPoints = Even_KeyPoints
            direction="Left"
        elif Json_File[0].get('32')[0] > Json_File[0].get('30')[0]:
            Index_Of_KeyPoints = Odd_KeyPoints
            direction= "Right"

        for i in range (len(Json_File)):
                shoulder_y_value=Json_File[i].get(Index_Of_KeyPoints[0])[1]
                hip_y_value=Json_File[i].get(Index_Of_KeyPoints[1])[1]
                Knee_y_value=Json_File[i].get(Index_Of_KeyPoints[2])[1]  
                ankle_y_value=Json_File[i].get(Index_Of_KeyPoints[3])[1]             
                
                shoulder_x_value=Json_File[i].get(Index_Of_KeyPoints[0])[0]
                hip_x_value=Json_File[i].get(Index_Of_KeyPoints[1])[0]
                Knee_x_value=Json_File[i].get(Index_Of_KeyPoints[2])[0]
                ankle_x_value=Json_File[i].get(Index_Of_KeyPoints[3])[0]
                Toes_x_value=Json_File[i].get(Index_Of_KeyPoints[5])[0]
                
                Shoulder_Y_Positions.append(shoulder_y_value)
                Hip_Y_Positions.append(hip_y_value)
                Knee_Y_Positions.append(Knee_y_value)
                Ankle_Y_Positions.append(ankle_y_value)

                Shoulder_X_Positions.append(shoulder_x_value)
                Hip_X_Positions.append(hip_x_value)
                Knee_X_Positions.append(Knee_x_value)
                Ankle_X_Positions.append(ankle_x_value)
                Toes_X_Positions.append(Toes_x_value)


    '''
    remove the dublicated numbers of adjacents' indecies 
    '''
    for i in range(len(Hip_Y_Positions)):
        currentNum = Hip_Y_Positions[i]
        if i < len(Hip_Y_Positions)-1:
            nextNum = Hip_Y_Positions[i+1]
        if currentNum != nextNum:
            New_Hip_Y_Positions.append(Hip_Y_Positions[i])
        elif currentNum == nextNum:
            Indecies_Of_Deleted_Values.append(i)

    """
        Get The Max & Min Values of hip joint and the corresponding indices after removing
        repeated numbers
    """
    for i in range(0, len(New_Hip_Y_Positions)):
        prev = New_Hip_Y_Positions[i-1]
        currentvalue = New_Hip_Y_Positions[i]

        if i < len(New_Hip_Y_Positions)-1:
            next = New_Hip_Y_Positions[i+1]

        if (prev > currentvalue < next) and (currentvalue < (np.mean(New_Hip_Y_Positions))):
            Min_Y_Hip.append(currentvalue)
            Min_index.append(i)

        elif (prev < currentvalue > next) and (currentvalue > (np.mean(New_Hip_Y_Positions))):
            Max_Y_Hip.append(currentvalue)
            Max_index.append(i)
    
    New_Max_Y_Hip=list(set(Max_Y_Hip))
    New_Min_Y_Hip=list(set(Min_Y_Hip))


    """
        Get The indices of Max & Min Values of hip joint from thr original list
    """
    for index in range (len(Hip_Y_Positions)):
        for max_index in range (len(New_Max_Y_Hip)):
            if Hip_Y_Positions[index]==New_Max_Y_Hip[max_index]:
                original_indecies_max.append(index)
        for min_index in range (len(New_Min_Y_Hip)):
            if Hip_Y_Positions[index]==New_Min_Y_Hip[min_index]:
                original_indecies_min.append(index)
    return direction


def Comparing_Algorithm(jsonPath):
    Direction_Side=Extract_Positions_Of_KeyPoints(jsonPath)

    if Direction_Side=="Left":
        for min_index in (original_indecies_min):
            # check Knee Position
            if Knee_X_Positions[min_index] > Toes_X_Positions[min_index]:
                Knee_WRT_Toes_25_26.append(1)
                Knee_Notes.append('Correct Knee Position')
            
            else:
                Knee_WRT_Toes_25_26.append(0)
                Knee_Notes.append('Wrong Knee Position,your knee should not exceed your toes' )
            
            # check hip position
            
            if ((0.85*Knee_Y_Positions[min_index]) <Hip_Y_Positions[min_index] <(1.15*Knee_Y_Positions[min_index])):
                Hip_WRT_Knee_23_24.append(1)
                Hip_Notes.append('Correct Hip position')
            
            else:
                Hip_WRT_Knee_23_24.append(0)
                Hip_Notes.append('Wrong Hip position,Your Hip should be at least at knee position')
            
            # Angle between hip&knee at min position
            knee_Angle=Knee_Angle(min_index)
            Min_Hip_Knee_Angles.append(knee_Angle)
            if 70<= knee_Angle <=110:
                Min_Knee_Angle_Status.append(1)
                KneeAngle_Notes.append('Correct knee angle')
            
            else :
                Min_Knee_Angle_Status.append(0)
                KneeAngle_Notes.append('Wrong knee angle,Your knee angle should be between 70 and 110 degree')
            
            #Angle of back at Min position
            
            Hip_Angle=Back_Angle(min_index)
            Min_Back_Angle.append(90-Hip_Angle)
            if 70<= (90-Hip_Angle) <= 90:
                Min_Back_Angle_Status.append(1)
                MinBackAngle_Notes.append('Correct Back angle')
            
            else:
                Min_Back_Angle_Status.append(0)
                MinBackAngle_Notes.append('Wrong Back angle,Your Back Angle should be between 70 and 90 degree')
            
        
        for max_index in (original_indecies_max):
            #Angle of back at Max position
            Hip_Angle=Back_Angle(max_index)
            Max_Back_Angle.append(180-Hip_Angle)
            
            if 160<= (180-Hip_Angle) <= 180:
                Max_Back_Angle_Status.append(1)
                MaxBackAngle_Notes.append('Correct Back angle')
            
            else:
                Max_Back_Angle_Status.append(0)        
                MaxBackAngle_Notes.append('Wrong Back angle,Your Back Angle should be between 160 and 180 degree')

    elif Direction_Side== "Right":
        for min_index in (original_indecies_min):
            # check knee position
            if Knee_X_Positions[min_index] < Toes_X_Positions[min_index]:
                Knee_WRT_Toes_25_26.append(1)    
                Knee_Notes.append('Correct Knee Position')
            
            else:
                Knee_WRT_Toes_25_26.append(0)
                Knee_Notes.append('Wrong Knee Position,your knee should not exceed your toes' )
            
            # check hip position
            if ((0.85*Knee_Y_Positions[min_index]) <= Hip_Y_Positions[min_index] <= (1.15*Knee_Y_Positions[min_index])):
                Hip_WRT_Knee_23_24.append(1)
                Hip_Notes.append('Correct Hip position')
            
            else:
                Hip_WRT_Knee_23_24.append(0)
                Hip_Notes.append('Wrong Hip position,Your Hip should be at least at knee position')

            
            # Angle between hip&knee at min position
            knee_Angle=Knee_Angle(min_index)
            Min_Hip_Knee_Angles.append(knee_Angle)
            if 70<= knee_Angle <=110:
                Min_Knee_Angle_Status.append(1)
                KneeAngle_Notes.append('Correct knee angle')
            
            else :
                Min_Knee_Angle_Status.append(0)
                KneeAngle_Notes.append('Wrong knee angle,Your knee angle should be between 70 and 110 degree')
            
            # Angle of back at Min position
            Hip_Angle=Back_Angle(min_index)
            Min_Back_Angle.append(90-Hip_Angle)

            if 70<= (90-Hip_Angle) <= 90:
                Min_Back_Angle_Status.append(1)
                MinBackAngle_Notes.append('Correct Back angle')

            else:
                Min_Back_Angle_Status.append(0)
                MinBackAngle_Notes.append('Wrong Back angle,Your Back Angle should be between 70 and 90 degree')

        # Angle between back at max position
        for max_index in (original_indecies_max):
            
            Hip_Angle=Back_Angle(max_index)
            Max_Back_Angle.append(180-Hip_Angle)
            
            if 160<= (180-Hip_Angle) <= 180:
                Max_Back_Angle_Status.append(1)
                MaxBackAngle_Notes.append('Correct Back angle')

            else:
                Max_Back_Angle_Status.append(0)   
                MaxBackAngle_Notes.append('Wrong Back angle,Your Back Angle should be between 160 and 180 degree')

    return original_indecies_max,original_indecies_min,Knee_WRT_Toes_25_26,Knee_Notes,Hip_WRT_Knee_23_24,Hip_Notes,Min_Knee_Angle_Status,KneeAngle_Notes,Max_Back_Angle_Status,MaxBackAngle_Notes,Min_Back_Angle_Status,MinBackAngle_Notes            

start=time.time()        
# Comparing_Algorithm() 
end=time.time()        
print('time=',(end-start))
print('direction',Direction)
# print('HipYPosition=',Hip_Y_Positions)
# print('Max',Max_index)
# print('Min',Min_index)
# print('NewMax_Y_Hip',New_Max_Y_Hip)
# print('NewHip',New_Hip_Y_Positions)
# print('Indecies_Of_Deleted_Values',Indecies_Of_Deleted_Values)
# print('maxIndicies=',original_indecies_max)
# print('minIndicies=',original_indecies_min)

# print('direction',Direction)


print('Knee_WRT_Toes', Knee_WRT_Toes_25_26)
# print('kneeNotes',Knee_Notes)
print('Hip_WRT_Knee', Hip_WRT_Knee_23_24)
# print('HipNotes',Hip_Notes)

# # print('Min_Hip_Knee_Angles', Min_Hip_Knee_Angles)
print('Min_Knee_Angle_Status', Min_Knee_Angle_Status)
# print('kneeAngleNotes',KneeAngle_Notes)

# # print('maxback',Max_Back_Angle)
# # print('minback',Min_Back_Angle)
print('Min_Back_Status',Min_Back_Angle_Status)
# print('MinBackNotes',MinBackAngle_Notes)

print('Max_Back_Status',Max_Back_Angle_Status)
# print('MaxBackNotes',MaxBackAngle_Notes)


# print('max_index',original_indecies_max)
# print('min_index',original_indecies_min)


# plt.subplot(121)
# plt.plot(Hip_Y_Positions, color='r', label='Hip_joint')

# plt.ylabel("Y-Values")
# plt.title("Tracking y_positions of four different joints")


# plt.legend(loc='upper right')

# plt.show()
