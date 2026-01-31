# Maltese Traffic Sign Object and Attribute Detector

A comprehensive machine learning project for detecting and classifying Maltese traffic signs with multiple object detection models and attribute classification systems. This project was developed as part of the ARI3129 course assignment.

## Overview

This repository implements a complete pipeline for traffic sign detection and attribute recognition specifically tailored for Maltese traffic signs. The project compares multiple state-of-the-art object detection architectures and includes specialized classifiers for various traffic sign attributes.

## Features

- **Multiple Object Detection Models**
- **Attribute Classification**: Specialized classifiers for:
  - Sign shape detection
  - Mounting type recognition
  - Viewing angle classification
  - Sign condition detector
- **Data Visualization**: Comprehensive analysis and visualisation of the dataset
- **Performance Comparison**: Side-by-side evaluation of different model architectures

## Repository Structure

```
├── Dataset/
│   ├── DC/          # Damian Cutajar's dataset contribution
│   ├── MB/          # Miguel Baldacchino's dataset contribution
│   ├── MF/          # Matthew Farrugia's dataset contribution
│   └── PS/          # Pawlu Spiteri's dataset contribution
├── Scripts/
│   ├── 1_data_visualisation.ipynb
│   ├── 2a_Object_Detector_YOLOv8_Matthew_Farrugia.ipynb
│   ├── 2a_Object_Detector_YOLOv11_Miguel_Baldacchino.ipynb
│   ├── 2a_Object_Detector_YOLO12_Pawlu_Spiteri.ipynb
│   ├── 2a_Object_Detector_R_CNN_Damian_Cutajar.ipynb
│   ├── 2b_Mounting_Type_Miguel_Baldacchino.ipynb
│   ├── 2b_Sign_Shape_Damian_Cutajar.ipynb
│   ├── 2b_Viewing_Angle_Matthew_Farrugia.ipynb
│   ├── 2b_Sign_Condition_Pawlu_Spiteri.ipynb
│   ├── 2c_Results_Comparison.ipynb
│   └── Outputs/     # Model outputs and results
└── ARI3129 - Assignment Materials/
```

## Models Implemented

### Object Detection (2a)
1. **YOLOv8s**
2. **YOLOv11n**
3. **R-CNN**
4. **YOLO12n**

### Attribute Classification (2b)
1. **Mounting Type Classifier**
2. **Sign Shape Classifier**
3. **Viewing Angle Classifier**
4. **Sign Condition Classifier**


## Dataset

The dataset contains Maltese traffic sign images collected and annotated by team members:
- **DC**: Damian Cutajar's contributions
- **MB**: Miguel Baldacchino's contributions  
- **MF**: Matthew Farrugia's contributions
- **PS**: Pawlu Spiteri's contributions

Images are annotated with bounding boxes and attribute labels for comprehensive training.

## Team Members

- **Miguel Baldacchino** - YOLOv11n implementation, Mounting Type classification
- **Damian Cutajar** - R-CNN implementation, Sign Shape classification
- **Matthew Farrugia** - YOLOv8s implementation, Viewing Angle classification
- **Pawlu Spiteri** - YOLO12n implementation, Sign Condition classification

## Course Information

**Course**: ARI3129 - Computer Vision and Deep Learning  
**Project Type**: Assignment - Traffic Sign Detection and Classification

## Results

Detailed performance metrics, confusion matrices, and comparative analysis are available in the `2c_Results_Comparison.ipynb` notebook. Key evaluation metrics include:
- Mean Average Precision (mAP)
- Precision and Recall
- Inference speed
- Classification accuracy for attributes