import cv2
import os
input_path = "F:\\data_annotation\\frames extraction\\video_data\\white\\"
filename = 'IMG_0342.MOV'
output_path = "F:\\data_annotation\\frames extraction\\temp\\"

cap = cv2.VideoCapture(input_path + filename)  # FOR INPUT DATASET

first_file_name = 1752      # must be int value
scale_parameter_saving = 100
scale_parameter_display = 60
cap.set(1, 200)


while 1:
    ret, frame = cap.read()
    if ret:

        width = int(frame.shape[1] * scale_parameter_saving / 100)
        height = int(frame.shape[0] * scale_parameter_saving / 100)
        dim = (width, height)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        # resized = cv2.resize(frame, (int(frame.shape[1] * scale_parameter_display / 100), int(frame.shape[0] * scale_parameter_display / 100)), interpolation=cv2.INTER_AREA)

        cv2.imwrite(output_path + str(first_file_name) + '.jpg', frame)
        print(output_path + str(first_file_name) + '.jpg')
        first_file_name = first_file_name + 1
        # cv2.imshow("frames", frame)
        keyboard = cv2.waitKey(1)
        if keyboard == 'q' or keyboard == 27:
            break
    else:
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()