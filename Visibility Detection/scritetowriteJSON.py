import os
import json
import time


# open the folder results and write the txt file contents into a new json file
def writeJSON():
    # open the folder results
    dict= {}
    base = os.path.join(os.getcwd(), 'results')
    # get the list of files in the folder
    files = os.listdir(base)
    # print(files)
    for i in range(len(files)):
        folder = os.path.join(base, files[i])
        # print(folder)
        files1 = os.listdir(folder)
        # print(files1)
        req_file = os.path.join(folder, files1[1])
        # print(req_file)
        # write the contents in req_file into a new json file
        with open(req_file, 'r') as f:
            data = f.read()
            s = {}
            s["vis"] = data
            # current time stamp
            x = time.time()
            # convert x into a readable format
            y = time.ctime(x)
            s["time"] = y
            dict["test"+str(i)] = s
    with open('data.json', 'w') as f:
        json.dump(dict, f)
        print("JSON file created successfully!")



writeJSON()