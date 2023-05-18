import cv2
import os
from os.path import exists
import re
import msvcrt as m


def wait():
    m.getch()


input_path = "D:\\data_for_haarcascade\\haarcascade\\cascade_version_5\\New folder\\"
output_path = "D:\\data_for_haarcascade\\haarcascade\\cascade_version_5\\p\\"


for fname in sorted(os.listdir(input_path)):
    if fname.endswith(".png"):
        digit = fname.split('.p')
        img = cv2.imread(input_path + digit[0] + '.png')
        dh, dw, _ = img.shape

        f = open(input_path + digit[0] + '.txt', "r")
        img_txt = f.read()
        numbers = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", img_txt)

        _ = float(numbers[0])
        xx = float(numbers[1])
        yy = float(numbers[2])
        ww = float(numbers[3])
        hh = float(numbers[4])

        x = int((xx - ww / 2) * dw)
        r = int((xx + ww / 2) * dw)
        y = int((yy - hh / 2) * dh)
        b = int((yy + hh / 2) * dh)

        if x < 0:
            x = 0
        if r > dw - 1:
            r = dw - 1
        if y < 0:
            y = 0
        if b > dh - 1:
            b = dh - 1

        w = r - x
        h = b - y

        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        # cv2.imshow('img', img)
        print(fname)
        cropped_image = img[y: y + w + 20, x: x + h]
        im_path = output_path + digit[0] + '.png'
        cv2.imwrite(im_path, cropped_image)
cv2.waitKey(0)
