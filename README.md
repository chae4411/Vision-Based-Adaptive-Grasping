###### **Vision-Based Adaptive Grasping** 

A real-time computer vision system that analyzes segmented objects and estimates suitable grasp strategies and grasp points based on their geometric features.



The project uses webcam input and instance segmentation to detect objects in real time. Geometric properties such as object area, centroid, dimensions, aspect ratio, and orientation are extracted from segmentation masks. These features are then used to determine an appropriate grasp strategy and estimate potential grasp points.



###### **Project Goal**

The goal of this project is to develop a vision-based grasp planning pipeline without relying on a physical robotic arm.



Instead of directly controlling robotic hardware, the system focuses on the perception and planning stages of robotic grasping:

Camera Input -> Object Segmentation -> Geometric Feature Analysis -> Grasp Strategy Selection -> Grasp Point Estimation



###### **Current Features** 

* Real-time webcam input using OpenCV
* Instance segmentation using YOLO
* Segmentation mask extraction
* Object contour analysis
* Geometric feature extraction
* Object centroid calculation
* Object dimension and aspect ratio estimation
* Object orientation estimation



###### **Planned Features** 

* Rule-based grasp strategy selection
* Grasp point estimation based on object geometry
* Visualization of predicted grasp points
* Support for multiple grasp strategies
* Grasp planning evaluation on different object shapes



###### **Project Structure** 

main.py — Runs the real-time vision pipeline

vision/camera.py — Handles webcam input

vision/detector.py — Performs object segmentation

vision/object\_analyzer.py — Extracts geometric features from segmentation masks

tests/ — Contains project tests



###### **Technologies** 

Python

OpenCV

Ultralytics YOLO

NumPy



###### **Motivation**

Robotic grasping requires more than simply detecting an object. A grasp planning system must analyze the shape, size, and orientation of an object to determine how and where it should be grasped. 



This project focuses on the computer vision and grasp planning components of robotic manipulation by transforming segmentation results into geometric information that can be used for grasp decision-making.

