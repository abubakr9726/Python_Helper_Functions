import cv2
import os
input_path = "C:\\Users\\Admin\\Desktop\\cascade_version_2\\"
output_path = "C:\\Users\\Admin\\Desktop\\cascade_version_2\\n\\"

count = 0

for fname in sorted(os.listdir(input_path)):
        if fname.endswith(".png") or fname.endswith(".jpg") or fname.endswith(".jpeg"):
            img =  cv2.imread(input_path + fname)
            # img = cv2.resize (img, (600, 600), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(output_path + str(count) + '.jpg', img)
            count = count + 1

print(count)