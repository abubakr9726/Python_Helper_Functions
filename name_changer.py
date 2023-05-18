import cv2
import os

input_path = "F:\\data_annotation\\frames extraction\\white ball\\"
output_path = "F:\\data_annotation\\frames extraction\\white ball to annotate\\"

count = 1
for fname in sorted(os.listdir(input_path)):
    if fname.endswith(".jpg"):
        img = cv2.imread(input_path + fname)
        print(input_path + fname)
        # cv2.imshow('img', img)
        cv2.imwrite(output_path + str(count) + ".jpg", img)
        # os.rename(input_path + fname, output_path + str(count) + ".txt")
        count += 1

# count = 3760
# for fname in sorted(os.listdir(input_path)):
#     if fname.endswith(".txt"):
#         # img = cv2.imread(input_path + fname)
#         print(input_path + fname)
#         # cv2.imshow('img', img)
#         # cv2.imwrite(output_path + str(count) + ".jpg", img)
#         os.rename(input_path + fname, output_path + str(count) + ".txt")
#         count += 1
# print(count)