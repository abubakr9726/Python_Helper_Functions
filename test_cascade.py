import cv2

path_to_xml_file = 'cascade_v5.xml'

# cap = cv2.VideoCapture('C:\\Users\\Admin\\Desktop\\Videos_Recorded\\IMG_0074.MOV')  # FOR LIVE VIDEO FROM IP WEB CAM
# cap.set(1, 500)
cap = cv2.VideoCapture('http://192.168.179.67:8080/video')  # FOR LIVE VIDEO FROM IP WEB CAM
ballCascade = cv2.CascadeClassifier(path_to_xml_file)
print('hh')
imgwidth = 640
imgheight = 480
while 1:

    ret, img = cap.read()
    if ret:
        img = cv2.resize(img, (imgwidth, imgheight))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = ballCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(1, 1),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        # if w*h < 5000.0:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('img', img)

    keyboard = cv2.waitKey(1)
    if keyboard == 'q' or keyboard == 27:
        break
cv2.destroyAllWindows()