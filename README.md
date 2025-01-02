# Object-Detection-Using-Yolo

To run the project you need to install some libraries like
1. Open Cv    pip install opencv-python
2. ultralytics from Yolo  --pip install ultralytics
3. Torch Vision Latest Version  --pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

Download the Model File
If you don’t have the file, download the pre-trained YOLO model weights. Use one of the following YOLOv8 pre-trained models:
YOLOv8n (nano, lightweight)
YOLOv8s (small)
YOLOv8m (medium)
YOLOv8l (large)
YOLOv8x (extra-large)
Download a model (e.g., yolov8n.pt) from the official Ultralytics site: 
or in terminal:
yolo download model=yolov8n.pt

only you need to change the directory(path) of the model in place of model variable in read mode
like: 
model = YOLO(r'D:\Project file\Object Detection Using Yolo\Object Detection using Yolo Model\model.pt')

~Thank you
Santosh Kumar
