import cv2
import os
from os.path import exists
import time

cap = cv2.VideoCapture('http://192.168.18.149:4747/video')  # FOR LIVE VIDEO FROM IP WEB CAM


imgwidth = 600
imgheight = 600

output_dir = 'D:\\data_for_haarcascade\\'
folder_counter = 0

while exists((output_dir + str(folder_counter))):
    folder_counter += 1
os.mkdir((output_dir + str(folder_counter)))
frame_count = 0

while 1:
    ret, img = cap.read()
    frame_count = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    if ret:
        print(frame_count)
        img = cv2.resize(img, (imgwidth, imgheight))
        if frame_count % 5 == 0:
            out_file = output_dir + str(folder_counter) + '\\' + str(time.time()) + '.png'
            cv2.imwrite(out_file, img)
        cv2.imshow('img', img)


    keyboard = cv2.waitKey(1)
    if keyboard == 'q' or keyboard == 27:
        break
cv2.destroyAllWindows()
