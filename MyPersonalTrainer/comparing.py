import json
import random
import os
from Final_Version_Comparing_Algorithm import Comparing_Algorithm
import requests

cwd = os.path.dirname(os.path.realpath(__file__))
dir_n_files = os.listdir(cwd)
for j in range(0,len(dir_n_files),1):
    if dir_n_files[j].endswith('.json'):
        jsonPath=r'{}\{}'.format(cwd, dir_n_files[j])
        jsonFile=open(jsonPath)
        data = json.load(jsonFile)
        output=Comparing_Algorithm(jsonPath)
        print(output)
        True_Min_index=output[1]
        True_Max_index=output[0]
        Status_of_Min_Hip_Knee_Angles=output[6]
        Max_Back_Angle_Status=output[8]
        Min_Back_Angle_Status=output[10]
        Knee_WRT_Toes_25_26=output[2]
        Hip_WRT_Knee_23_24=output[4]

        for i in range(0,len(data),1):
            if i in True_Min_index:
                k=True_Min_index.index(i)
                data[i-1].update({"Angles":[Status_of_Min_Hip_Knee_Angles[k],Min_Back_Angle_Status[k]],"Positions":[Knee_WRT_Toes_25_26[k],Hip_WRT_Knee_23_24[k]]})
            elif i in True_Max_index:
                k=True_Max_index.index(i)
                data[i-1].update({"Angles":[1,Max_Back_Angle_Status[k]],"Positions":[1,1]})
            else:
                data[i-1].update({"Angles":[2,2],"Positions":[2,2]})
        with open(jsonPath, 'w') as fp:
            fp.write(
                '[' +
                ',\n'.join(json.dumps(i,separators=(',', ':')) for i in data) +
                ']\n')
url = 'http://127.0.0.1:8000/postStatus/'
myobj = {'Progress': 'Done'}
done = requests.post(url, json = myobj)