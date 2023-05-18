from ultralytics import YOLO
import cv2
from matplotlib import pyplot as plt


# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model

# Predict with the model
result = model.predict("bus.jpg", show=True, imgsz=640, conf=0.5, hide_labels=True, retina_masks=True)

print(result)

cv2.waitKey(0)


