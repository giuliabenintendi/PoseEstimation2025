# YOLOv11 Pose Estimation 2025

This project utilizes Ultralytics, YOLOv11 and OpenCV to perform real-time pose detection via a webcam. Follow the instructions below to set up the environment and run the script on **macOS** or **Windows**.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)

## Description

The YOLOv11 Pose Detection Script leverages the YOLOv8 model for real-time pose estimation using a webcam feed. This script is designed to be cross-platform, supporting both macOS and Windows systems.

## Installation

#### Prerequisites

- Python (preferably installed via Miniconda or Anaconda)
- A working webcam

#### Steps

1. **Create the Environment**:

   Open a terminal and run the following commands:

   ```bash
   conda create --name yolov8 python=3.9
   conda activate yolov8
2. Install Dependencies: Use pip to install the required Python packages:
    ```bash
    pip install -r requirements.txt 
3. Make sure the yolo11n-pose.pt file is in the same directory as the script. Then run:
   ```bash
   python yoloV11.py
   
### Usage

After completing the installation steps for your operating system, execute the script as described. The script will open a window displaying the webcam feed with real-time pose detection overlays.

## Notes

- **Stopping the Script**: Press `q` in the script window to quit.
- **Webcam Setup**: Ensure your webcam is connected and accessible by your system.
- **Model File**: The `yolo11n-pose.pt` file is included in the repository and required for the script to work. Ensure it is in the same directory as the script.
- **Cross-Platform Compatibility**: Ensure the environment is created correctly on macOS (with MPS) or Windows (with CUDA or CPU).

If you encounter issues, feel free to open an issue in the repository.
## License
The code in this repository is provided as-is, without any warranty. This project uses the following libraries, which are licensed under their respective terms:

- **Ultralytics**: Licensed under the [GPL-3.0 License](https://github.com/ultralytics/ultralytics/blob/main/LICENSE).
- **OpenCV**: Licensed under the [Apache License 2.0](https://github.com/opencv/opencv/blob/master/LICENSE).
- **NumPy**: Licensed under the [BSD 3-Clause License](https://github.com/numpy/numpy/blob/main/LICENSE.txt).

Please ensure compliance with these licenses if redistributing or modifying this project.
