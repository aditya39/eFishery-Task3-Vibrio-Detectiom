import clearml
from ultralytics import YOLO

import os
HOME = os.getcwd()
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


# Login ClearML
clearml.browser_login()

task = clearml.Task.init(
    project_name='Vibrio',    # project name of at least 3 characters
    task_name='Vibrio_Training_YOLOv8_Nano', # task name of at least 3 characters
    task_type="training",
    tags=["YOLOv8", "Nano"]  
)



from roboflow import Roboflow
rf = Roboflow(api_key="74Pb2GaCvTDY3KSnoxeK")
project = rf.workspace("wiranda-aditiya-znixh").project("vibrio-dt175")
dataset = project.version(3).download("yolov8")

model_handle = YOLO("yolov8n.pt")

# Use the model
results = model_handle.train(
    data=os.path.join(dataset.location, "data.yaml"),
    batch=6,
    device=0,
    epochs=200,
    workers=0,
    patience=100,
    imgsz=640)  # train the model