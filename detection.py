from ultralytics import YOLO
import cv2
import numpy as np
import yaml

# Open config.yaml File
with open("config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

area = 7854 # real size area of the cawan petri
frame_size = 640*640 # image input size

# Object detection function, input is image & model
def detect(file, model):
    # initiate list of vibrio size
    list_black_vibrio_size = []
    list_green_vibrio_size = []
    list_yellow_vibrio_size = []
    
    # Convert File byte to array for OpenCV 
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Inference YOLOv8
    result = model.predict(
        source=image, # image input
        conf=cfg["yolov8"]["conf"], # confidence threshold
        device=cfg["yolov8"]["device"]) # device (defualt 0 (gpu), change to "cpu" to use cpu)
    
    # Plot detection result image
    img_yolo = result[0].plot()

    # Retrive result information
    prob = result[0].boxes.cls
    problist = prob.tolist() # change type from tensor to list
    countListDetected = [len(problist), problist.count(0.0), problist.count(1.0), problist.count(2.0)] # count total detected for each class

    # Retrive boundingbox information
    boxes = result[0].boxes.xywh # get list xywh for each detected object
    boxes_list = boxes.tolist() # change type from tensor to list

    # Categories Size For Each Vibrio
    n = 0
    for x in boxes_list: # Loop for each detected vibrio
        vibrio_class = int(problist[n])
        w = float(boxes_list[n][2])
        h = float(boxes_list[n][3])
   
        # list each vibrio by its color
        if vibrio_class == 0: # black vibrio
            size = (w*h) * (area/frame_size) # calculate real estimate size in milimeter
            list_black_vibrio_size.append(size)
        if vibrio_class == 1: # green vibrio
            size = (w*h) * (area/frame_size) # calculate real estimate size in milimeter
            list_green_vibrio_size.append(size)
        if vibrio_class == 2: # yellow vibrio
            size = (w*h) * (area/frame_size) # calculate real estimate size in milimeter
            list_yellow_vibrio_size.append(size)
        n+=1

    # Categories Vibrio
    # Black
    smallBlack = len([x for x in list_black_vibrio_size if x < 100])
    mediumBlack = len([x for x in list_black_vibrio_size if x > 100 and x < 200])
    largeBlack = len([x for x in list_black_vibrio_size if x > 200])

    # Green
    smallGreen = len([x for x in list_green_vibrio_size if x < 100])
    mediumGreen = len([x for x in list_green_vibrio_size if x > 100 and x < 200])
    largeGreen = len([x for x in list_green_vibrio_size if x > 200])

    # Yellow
    smallYellow = len([x for x in list_yellow_vibrio_size if x < 100])
    mediumYellow = len([x for x in list_yellow_vibrio_size if x > 100 and x < 200])
    largeYellow = len([x for x in list_yellow_vibrio_size if x > 200])

    # Create dictionary contain of all categorical vibrio
    vibrio_size = {"smallBlack":smallBlack,
                   "mediumBlack":mediumBlack,
                   "largeBlack":largeBlack,
                   "smallGreen":smallGreen,
                   "mediumGreen":mediumGreen,
                   "largeGreen":largeGreen,
                   "smallYellow":smallYellow,
                   "mediumYellow":mediumYellow,
                   "largeYellow":largeYellow}
    
    return vibrio_size, countListDetected, img_yolo



