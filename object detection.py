from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model.predict(source="0" , imgsz= 300, conf=0.6, show =True)
