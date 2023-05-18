import cv2
import os
import time


start_time = time.time()

input_path = "F:\\Spark Games Cricket app everything\\Ball data\\Video Data\\18_05\\"
output_path = "F:\\data_annotation\\frames extraction\\temp\\"


file_paths = []
for file_name in os.listdir(input_path):
    file_paths.append(os.path.join(input_path, file_name))
print(len(file_paths))

first_file_name = 573      # must be int value
for singlefilepath in file_paths:
    print(singlefilepath, "---------->>> file number:", file_paths.index(singlefilepath)+1)
    cap = cv2.VideoCapture(singlefilepath)  # FOR INPUT DATASET

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(output_path + str(first_file_name) + '.jpg', frame)
            print(output_path + str(first_file_name) + '.jpg')
            first_file_name = first_file_name + 1
            keyboard = cv2.waitKey(1)
            if keyboard == 'q' or keyboard == 27:
                break
        else:
            break
    # When everything done, release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()

end_time = time.time() - start_time
print(f"Total time taken for processing {len(file_paths)} file: {end_time}")