# Vision-Based Adaptive Grasping

**Status: Work in Progress (Personal Project)**

This is an ongoing personal project exploring computer vision-based object segmentation and grasp planning using Python, OpenCV, and Ultralytics YOLO.

The project currently contains experimental implementations of object analysis and rule-based grasp planning. The complete system has not yet been finalized or systematically evaluated.

## Project Overview

This project explores a vision-based system that analyzes segmented objects and estimates potential grasp strategies and contact points based on their geometric features.

The system uses webcam input and a pretrained YOLO segmentation model to detect objects. Geometric properties such as object area, centroid, dimensions, aspect ratio, and orientation are extracted from segmentation masks.

These features are then used to select a grasp strategy and estimate candidate contact points.

## Project Goal

The goal of this project is to develop a vision-based grasp planning pipeline without relying on a physical robotic arm.

Instead of directly controlling robotic hardware, the system focuses on the perception and planning stages of robotic grasping:

Camera Input → Object Segmentation → Geometric Feature Analysis → Grasp Strategy Selection → Grasp Point Estimation → Visualization

## Current Features

The following features are implemented in the current codebase:

**Computer Vision**
- Webcam input using OpenCV
- Instance segmentation using a pretrained YOLO11 segmentation model
- Segmentation mask extraction
- Object contour analysis
- Object filtering based on class labels, detection confidence, and contour area

**Geometric Feature Analysis**
- Object area calculation
- Object centroid calculation
- Object dimension and aspect ratio estimation
- Object orientation estimation

**Grasp Planning**
- Rule-based grasp strategy selection based on object aspect ratio
- Candidate grasp point estimation using segmentation mask boundaries
- Support for power, pinch, spherical, and lateral grasp strategies

**Visualization**
- Detected object visualization
- Grasp line and contact point visualization
- Object centroid visualization
- Display of selected grasp strategy and orientation

These features have been implemented experimentally and have not yet undergone systematic testing or performance evaluation.

## Planned Features

- Improved grasp strategy selection and scoring
- Additional shape descriptors such as circularity and solidity
- Grasp quality evaluation
- More stable predictions across video frames
- Evaluation on different object shapes
- Automated tests for geometric feature extraction and grasp planning

## Project Structure

```text
Vision-Based-Adaptive-Grasping/
├── main.py
├── requirements.txt
├── README.md
├── planning/
│   ├── __init__.py
│   ├── grasp_types.py
│   ├── grasp_result.py
│   └── grasp_planner.py
└── vision/
    ├── __init__.py
    ├── camera.py
    ├── detector.py
    ├── object_analyzer.py
    └── visualizer.py
```

**Main Components**

- `main.py` — Runs the vision and grasp planning pipeline.
- `vision/camera.py` — Handles webcam input.
- `vision/detector.py` — Performs object segmentation using YOLO.
- `vision/object_analyzer.py` — Extracts geometric features from segmentation masks.
- `vision/visualizer.py` — Visualizes grasp lines, contact points, and planning results.
- `planning/grasp_types.py` — Defines supported grasp strategy types.
- `planning/grasp_result.py` — Defines the grasp planning result structure.
- `planning/grasp_planner.py` — Selects grasp strategies and estimates candidate contact points.

A `tests/` directory is planned for future automated testing.

## Technologies

- Python
- OpenCV
- Ultralytics YOLO11
- NumPy

## Development Approach

This is a personal learning and experimentation project developed with reference to publicly available computer vision and robotic grasping resources.

The implementation has been developed and adapted with the assistance of AI coding tools. Existing concepts and publicly available code examples have been used as references while adapting the implementation to the project's goals.

The project is intended to document an ongoing learning process rather than present an independently developed or fully validated grasp planning algorithm.

## Current Limitations

- Grasp strategies are selected using simple aspect-ratio-based rules.
- Candidate grasp points are estimated geometrically and have not been validated for physical grasp stability.
- Grasp strategy scores are predefined heuristic values rather than experimentally measured grasp quality scores.
- The system does not control a physical robotic arm.
- Automated tests and systematic performance evaluation have not yet been completed.
- Real-time performance and robustness across different environments have not been formally evaluated.

## Motivation

Robotic grasping requires more than simply detecting an object. A grasp planning system must analyze the shape, size, and orientation of an object to estimate how and where it should be grasped.

This project focuses on the computer vision and grasp planning components of robotic manipulation by transforming segmentation results into geometric information that can be used for grasp decision-making.
