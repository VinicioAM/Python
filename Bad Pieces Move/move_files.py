import datetime
import numpy as np
import cv2
import pytesseract
import os
import time

cfg_file = open('config.cfg', 'r').readlines()
tesseract_exe = cfg_file[1].replace("\n", "")
source_folder = cfg_file[3].replace("\n", "")
destination = cfg_file[5].replace("\n", "")
delay = int(cfg_file[7].replace("\n", ""))
folder_or_subfolder = cfg_file[9].replace("\n", "")
current_hour_or_last = cfg_file[11].replace("\n", "")
# count of ok and ko
count_ko = 0
count_ok = 0
# change \ to \\
pytesseract.pytesseract.tesseract_cmd = tesseract_exe.replace("\\", "\\\\")
# amount of boxes-1 in image to analyse
img = [""]*14
# def low and upper to create COLOR MASK
lower_green = np.array([144, 200, 144])
upper_green = np.array([144, 255, 144])
lower_red = np.array([0, 69, 0])
upper_red = np.array([0, 69, 255])
# def current date
curr_date = datetime.datetime.now().strftime("%d_%m_%Y")
# use folder os subfolder(current date)?
if folder_or_subfolder == 'SF':
    source_folder = str(source_folder) + "\\" + curr_date

# text wrinting config
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (515, 30)
fontScale = 1
fontColor = (0, 0, 0)
thickness = 2
lineType = 2

#################################### STARTING ############################
print("\n###CONFIG FILE###\n")
print(f"PyTesseract: {tesseract_exe}")
print(f"Source Folder: {source_folder}")
print(f"Destination Folder: {destination}")
print(f"Delay: {delay}")
print(f"Folder or SubFolder: {folder_or_subfolder}")
print(f"Last Hour or Current Day: {current_hour_or_last}")
print(f"\nStarting file transfer...\n")
time.sleep(1)

while True:
    # def current date
    curr_y = datetime.datetime.now().strftime("%Y")
    curr_m = datetime.datetime.now().strftime("%m")
    curr_d = datetime.datetime.now().strftime("%d")
    curr_h = datetime.datetime.now().hour
    curr_min = datetime.datetime.now().minute
    curr_sec = datetime.datetime.now().second
    curr_date = datetime.datetime.now().strftime("%d_%m_%Y")
    # if midnight, change to the lastday
    if curr_h == 00:
        #curr_d = str(int(curr_d) - 1)
        curr_d = str(int(curr_d) - 1)
        curr_date = curr_d + "_" + curr_m + "_" + curr_y
        curr_h = "23"
    # capture subfolders from source
    files = os.listdir(source_folder)
    start_time = datetime.datetime.now().strftime("%d/%m/%Y")+" - "+str(curr_h) + ":"+str(curr_min)+":"+str(curr_sec)+"...\n"
    print(f"\nStarting Transfer Cycle at: {start_time}")
    for file in files:
        if current_hour_or_last == "AT":
            origin = source_folder + "\\" + file
            main_img = cv2.imread(origin)
            img = cv2.imread(origin)[20:800, 260:290]
            img = cv2.inRange(img, lower_red, upper_red)  # red mask
            if np.count_nonzero(img) > 0:
                send_to = destination+"\\"+file
                count_ko += 1
                text = f"{file[15:17]}/{file[12:14]}/{file[7:11]} - {file[18:20]}:{file[21:23]}:{file[24:26]}"
                new = cv2.putText(main_img, text, bottomLeftCornerOfText,
                                  font, fontScale, fontColor, thickness, lineType)
                cv2.imwrite(send_to, new)
                print(f"KO: {file}")
            else:
                count_ok += 1
                print(f"OK: {file}")
        else:
            if current_hour_or_last == "LH":
                check_hour = int(curr_h) - 1
            else:
                check_hour = int(curr_h)
            if int(file[18:20]) == int(check_hour):
                origin = source_folder + "\\" + file
                main_img = cv2.imread(origin)
                img = cv2.imread(origin)[20:800, 260:290]
                img = cv2.inRange(img, lower_red, upper_red)  # red mask
                if np.count_nonzero(img) > 0:
                    send_to = destination+"\\"+file
                    count_ko += 1
                    text = f"{file[15:17]}/{file[12:14]}/{file[7:11]} - {file[18:20]}:{file[21:23]}:{file[24:26]}"
                    new = cv2.putText(main_img, text, bottomLeftCornerOfText,
                                      font, fontScale, fontColor, thickness, lineType)
                    cv2.imwrite(send_to, new)
                    print(f"KO: {file}")
                else:
                    count_ok += 1
                    print(f"OK: {file}")
    print(f"Total KO: {count_ko} of {count_ok + count_ko}")
    print(f"Transfer Cycle Finished. Next Cycle in {delay/60} minutes.") 
    time.sleep(delay)