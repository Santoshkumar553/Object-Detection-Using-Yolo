import cv2
from ultralytics import YOLO

## Loading yolo model
model = YOLO(r'D:\Project file\Object Detection Using Yolo\Object Detection using Yolo Model\model.pt')
print(model.names)

## here 0th index for own device camera capture
webcamera = cv2.VideoCapture(0)

## Check if the camera opened successfully
if not webcamera.isOpened():
    print("Falled to open the Webcam Please Verify and try angain......")
    exit()

while True:
    ## Capturing frame in cam
    success, frame = webcamera.read()
    if not success:
        print("Failed to capture frame from camera. Exiting...")
        break

    results = model.predict(frame, conf=0.8)
    frame_with_detections = results[0].plot()

    cv2.imshow("Laptop Camera - YOLO Object Detection", frame_with_detections)

    if cv2.waitKey(1) == ord('q'):
        break
webcamera.release()
cv2.destroyAllWindows()


## Documentation
'''
Project Name: Object Detection using Yolo
Created By: Santosh Kumar
Creating Date: 02.01.2025
'''