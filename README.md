# YOLOv11 Pose Estimation 

This project uses Ultralytics' YOLOv8 and OpenCV for real-time pose detection via a webcam. Follow the instructions below to set up the environment and run the script on **macOS** or **Windows**.

---

## macOS and Windows Installation

### Prerequisites
- Python (preferably installed via Miniconda or Anaconda)
- A working webcam

### Steps to Install and Run:

1. **Create the Environment**:
   Open a terminal and run the following commands:
   ```bash
   conda create --name yolov8 --file requirements.txt
   conda activate yolov8
2. Make sure the yolo11n-pose.pt file is in the same directory as the script. Then run:
   ```bash
   python yoloV11.py


## License
The code in this repository is provided as-is, without any warranty. This project uses the following libraries, which are licensed under their respective terms:

- **Ultralytics**: Licensed under the [GPL-3.0 License](https://github.com/ultralytics/ultralytics/blob/main/LICENSE).
- **OpenCV**: Licensed under the [Apache License 2.0](https://github.com/opencv/opencv/blob/master/LICENSE).
- **NumPy**: Licensed under the [BSD 3-Clause License](https://github.com/numpy/numpy/blob/main/LICENSE.txt).

Please ensure compliance with these licenses if redistributing or modifying this project.
