# import cv2
import os

input_path = "D:\\data_for_haarcascade\\red_ball\\"
output_path = "D:\\data_for_haarcascade\\red_ball\\"
sub_folder = "log\\"

if not os.path.exists(output_path + sub_folder):
    os.mkdir(output_path + sub_folder)

count = 0
sum = 0
for fName in sorted(os.listdir(input_path)):
    if fName.endswith(".txt"):
        with open(input_path + f"{count}.txt", 'r') as fp:
            data = len(fp.readlines())
            sum = data + sum
            # print('Total lines:', data)
            count += 1

f = open(output_path + sub_folder + "log.txt", "w")
f.write(f"Total number of trainable images: {count}\n")
f.write(f"Total numer of annotations: {sum}\n")