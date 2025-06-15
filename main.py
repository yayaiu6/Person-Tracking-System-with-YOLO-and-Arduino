import cv2
from ultralytics import YOLO
import torch
import serial
import time

# Initialize serial communication with Arduino
try:
    ser = serial.Serial('COM4', 9600)  # Adjust COM port as needed
    time.sleep(2)  # Wait for the connection to stabilize
except:
    print("Error connecting to Arduino")
    exit()

# Set device to GPU if available, otherwise CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
# Load YOLOv8 model and move to the specified device
model = YOLO('yolov8.pt').to(device)  
# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Set frame resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error opening the camera")
    exit()

# Define frame width and center threshold for motor control
FRAME_WIDTH = 640
CENTER_THRESHOLD = 120

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Perform object detection with YOLO model
    results = model(frame, conf=0.5, iou=0.7, device=device)

    person_detected = False
    for result in results:
        for box in result.boxes:
            # Check if detected object is a person
            if model.names[int(box.cls)] == 'person':
                person_detected = True
                # Extract bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf[0].item()

                # Calculate center of the bounding box
                center_x = (x1 + x2) // 2

                # Draw bounding box and confidence score on frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
                cv2.putText(frame, f'Person {confidence:.2f}', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

                # Determine motor movement based on person's position
                if center_x < (FRAME_WIDTH // 2 - CENTER_THRESHOLD):
                    # Person is on the left side -> move motor left
                    ser.write(b'L')
                    print("Moving left")
                elif center_x > (FRAME_WIDTH // 2 + CENTER_THRESHOLD):
                    # Person is on the right side -> move motor right
                    ser.write(b'R')
                    print("Moving right")
                else:
                    # Person is in the center -> stop motor
                    ser.write(b'S')
                    print("Stopped: Person in center")

    # If no person is detected, stop the motor
    if not person_detected:
        ser.write(b'S')
        print("Stopped: No person detected")

    # Display the frame with detections
    cv2.imshow('YOLO Detection', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
# Close serial connection
ser.close()