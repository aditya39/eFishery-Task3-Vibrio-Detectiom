import yaml
import numpy as np
import pandas as pd
import streamlit as st
from ultralytics import YOLO
from clearml import InputModel
from detection import detect
import os

os.environ['CLEARML_CONFIG_FILE'] = "clearml.conf"
# Open Config File
with open("config.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# Create Sidebar
with st.sidebar:
    st.title("Project 3 - Vibrio Detection") # Sidebar Title
    st.image("efisherylogolandscape.jpg") # Sidebar Logo
    st.divider()
    
    # Create select box to select YOLOv8 model
    st.header("Choose a Model")
    selectModel = st.selectbox("What YOLOv8 model you would like to choose?", 
                               ("YOLOv8 Nano", "YOLOv8 Small", "YOLOv8 Medium","YOLOv8 Large", "YOLOv8 Xtreme"))

    # If model selected, pick the model from ClearML IDModel
    if selectModel == "YOLOv8 Nano":
        model = InputModel(model_id=cfg["model"]["yolov8n"]) # model_id pickup from config.yaml
        store_model = model.get_local_copy()
        model = YOLO(store_model)

    if selectModel == "YOLOv8 Small":
        model = InputModel(model_id=cfg["model"]["yolov8s"])
        store_model = model.get_local_copy()
        model = YOLO(store_model)

    if selectModel == "YOLOv8 Medium":
        model = InputModel(model_id=cfg["model"]["yolov8m"])
        store_model = model.get_local_copy()
        model = YOLO(store_model)

    if selectModel == "YOLOv8 Large":
        model = InputModel(model_id=cfg["model"]["yolov8l"])
        store_model = model.get_local_copy()
        model = YOLO(store_model)

    if selectModel == "YOLOv8 Xtreme":
        model = InputModel(model_id=cfg["model"]["yolov8x"])
        store_model = model.get_local_copy()
        model = YOLO(store_model)

    # Create an expander which explain more about the models difference
    expander = st.expander("See explanation about the model..", expanded=False)
    expander.write("""Xtreme model give the most accuracy while sacrifice performance speed, Nano is the fastest model but least accurate.
    \nYou can check Yolov8 models comparation by expanding image below..
                   Visit YOLO8 github link for more, https://github.com/ultralytics/ultralytics""")
    expander.image("yolo8_detail.png")

    
# Main Page Container
with st.container():
    st.title("Vibrio Detection & Count With AI!")
    st.divider()

    # Create Browse File Action
    st.subheader("Upload Vibrio Image")
    file = st.file_uploader("Upload Your Vibrio Image Here", type=["jpg", "jpeg", "png"])

    # Check if file exist then call detect function by passing file image & model
    if file:
        # countListDetection consist of information how many for each vibrio class detected
        vibrio_size, countListDetected, img_yolo = detect(file, model) 

        # Create container for show image
        with st.container():
            col1, col2 = st.columns(2) # Create two columns to place the image
            with col1:
                st.image(file)
                st.markdown("<p style='text-align: center; color: white;'>Original Image</p>", unsafe_allow_html=True)
            with col2:
                st.image(img_yolo)
                st.markdown("<p style='text-align: center; color: white;'>Detected Vibro by YOLOv8</p>", unsafe_allow_html=True)
            st.divider()
                
        # Create container for result of detection 
        with st.container():
            st.header("Vibrio Detection Result")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Vibrio Detected", countListDetected[0])
            with col2:
                st.metric("Total Yellow Detected", countListDetected[3])
            with col3:
                st.metric("Total Green Detected", countListDetected[2])
            with col4:
                st.metric("Total Black Detected", countListDetected[1])
            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("Yellow Vibrio")
                st.write("Small Vibrio = ", vibrio_size["smallYellow"])
                st.write("Medium Vibrio = ", vibrio_size["mediumYellow"])
                st.write("Large Vibrio = ", vibrio_size["largeYellow"])

            with col2:
                st.subheader("Green Vibrio")
                st.write("Small Vibrio = ", vibrio_size["smallGreen"])
                st.write("Medium Vibrio = ", vibrio_size["mediumGreen"])
                st.write("Large Vibrio = ", vibrio_size["largeGreen"])

            with col3:
                st.subheader("Black Vibrio")
                st.write("Small Vibrio = ", vibrio_size["smallBlack"])
                st.write("Medium Vibrio = ", vibrio_size["mediumBlack"])
                st.write("Large Vibrio = ", vibrio_size["largeBlack"])

            # Create an expander which explain more about the models difference
            expander = st.expander("Click to see more explanation about vibrio size..", expanded=False)
            expander.subheader("Vibrio Categorization")
            expander.write("Small vibrio   : 0-100   mm")
            expander.write("Medium vibrio  : 100-200 mm")
            expander.write("Large vibrio   : > 200   mm")
                    
       
                
    

  