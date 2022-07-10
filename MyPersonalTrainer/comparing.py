import json
import random
import os


cwd = os.path.dirname(os.path.realpath(__file__))
dir_n_files = os.listdir(cwd)
for j in range(0,len(dir_n_files),1):
    if dir_n_files[j].endswith('.json'):
        jsonPath=r'{}\{}'.format(cwd, dir_n_files[j])
        jsonFile=open(jsonPath)
        data = json.load(jsonFile)
        for i in range(0,len(data),1):
            data[i].update({"Values":[round(random.random()),round(random.random()),round(random.random())]})
        newpath=r'{}\{}'.format(cwd, 'file2.json')
        with open(jsonPath, 'w') as fp:
            fp.write(
                '[' +
                ',\n'.join(json.dumps(i,separators=(',', ':')) for i in data) +
                ']\n')