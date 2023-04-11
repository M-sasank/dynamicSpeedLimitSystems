# resize the images present in D:\Sem6\PTP\dynamicSpeedLimitSystems\Visibility Detection\point_NUPT to 1920 x 1080
import os
import cv2

def resize():
    base = "D:\Sem6\PTP\dynamicSpeedLimitSystems\Visibility Detection\point_NUPT"
    thrBase = "D:\Sem6\PTP\dynamicSpeedLimitSystems\Visibility Detection\Road_surfaces"
    folders = os.listdir(base)
    # read files in the folder
    t = os.listdir(thrBase)
    # files in folders
    for i in range(len(t)):
        file = os.path.join(thrBase, t[i])
        img = cv2.imread(file)
        img = cv2.resize(img, (1920, 1080))
        cv2.imwrite(file, img)
    print("Successfully resized Road Images into 1920 x 1080")
    for i in range(len(folders)):
        files = os.listdir(os.path.join(base, folders[i]))
        file = os.path.join(base, folders[i], files[0])
        thr1= os.path.join(thrBase, t[i])
        img = cv2.imread(file)
        img = cv2.resize(img, (1920, 1080))
        cv2.imwrite(file, img)
    print("Successfully resized Input into 1920 x 1080")
