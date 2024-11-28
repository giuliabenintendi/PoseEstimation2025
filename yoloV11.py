# PER USARE QUESTO SCRIPT USARE CONDA yolov8

from ultralytics import YOLO
import cv2

# Load the YOLOv11 pose model
model = YOLO("yolo11n-pose.pt")

# Set device (optional)
device = 'cpu'  # Use 'cpu', 'cuda', or 'mps' for Apple Silicon

# Open a live webcam feed
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Set show=True to display the results
    results = model.predict(frame, show=True)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()