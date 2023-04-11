import os
import json
import serial

ser = serial.Serial("COM7", 115200)
# load the json file
with open('data.json', 'r') as f:
    json_data = json.load(f)

# convert json to dictionary
data_dict = dict(json_data)
vis_list = []
for i in data_dict:
    vis_list.append(int(data_dict[i]["vis"]))
min_vis = min(vis_list)
max_vis = max(vis_list)
min_speed = 20
max_speed = 60
# speed_limit = min_speed + (max_speed - min_speed) * (max_vis - data_dict["test0"]["vis"]) / (max_vis - min_vis)
# print(speed_limit)
while 1:
    print("Enter the index of the test image: (Enter -1 to exit): ")
    index = int(input())
    if index == -1:
        break
    if index <= 5:
        speed_limit = min_speed + (max_speed - min_speed) * (max_vis - vis_list[index]) / (max_vis - min_vis)
        # round off to 2 decimal
        speed_limit = round(speed_limit, 2)
        speed_limit = str(speed_limit)
        # print(type(speed_limit))
        # print(speed_limit)
        speed_limit = speed_limit + "kmph\r\n"
        ser.write(speed_limit.encode())
    else:
        ser.write("invalid index\r\n".encode())
# 1 4 3 0 2
