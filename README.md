# Autonomous Systems

Development of an autonomous vehicle perception pipeline using camera and LiDAR data.

## Project Overview

This project explores perception and sensor-based processing techniques for autonomous vehicles, progressing from RGB camera perception and object detection to LiDAR processing and multi-sensor fusion.

The repository contains practical experiments, Jupyter notebooks, analysis and implementation code developed throughout the project.

## Project Pipeline

### 1. Dataset Exploration
Initial exploration and analysis of the autonomous driving dataset.

### 2. RGB Perception
Development of a baseline camera-based perception approach.

### 3. YOLO Object Detection
RGB object detection experiments, model comparison and evaluation under different environmental conditions.

### 4. LiDAR Exploration
Analysis and exploration of LiDAR point cloud data.

### 5. Camera–LiDAR Projection
Projection and alignment experiments between camera images and LiDAR point clouds.

### 6. Sensor Fusion
Camera–LiDAR association and multi-sensor fusion experiments.

### 7. PointPillars
Exploration and testing of LiDAR-based 3D object detection using PointPillars.

## Repository Structure

```text
autonomous-systems/
├── notebooks/
│   ├── 01_dataset_exploration/
│   ├── 02_rgb_perception/
│   ├── 03_yolo_detection/
│   ├── 04_lidar_exploration/
│   ├── 05_camera_lidar_projection/
│   ├── 06_sensor_fusion/
│   └── 07_pointpillars/
├── src/
│   └── stage5/
├── results/
├── docs/
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies

- Python
- Jupyter Notebook
- YOLO
- LiDAR point cloud processing
- Camera–LiDAR sensor fusion
- PointPillars

## Data and Model Weights

Datasets, trained model weights, virtual environments and generated outputs are excluded from this repository due to their size.

## Project Status

In development.

## Author

Maritza
