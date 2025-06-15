# Person Tracking System with YOLO and Arduino

## Project Overview
This project is a real-time person tracking system that utilizes the YOLOv8 object detection model to detect and track a person in a video feed from a webcam. By analyzing the person's position within the frame, the system sends commands to an Arduino-controlled motor to adjust its direction (left, right, or stop), ensuring the person remains centered in the frame by rotating a platform or camera mount. The project combines advanced computer vision with hardware control to create a versatile and accessible tracking solution.

### Applications
The system is designed to be highly adaptable, with a wide range of potential applications across various domains. Below are some key applications, each accompanied by a practical example:

1. **Security and Surveillance**:
   - **Use Case**: Automatically track individuals in a monitored area, such as a restricted zone in a building.
   - **Example**: In a warehouse, the system can be mounted on a rotating camera platform to follow a person moving through aisles, ensuring continuous monitoring without manual camera adjustments. This is useful for detecting unauthorized access or tracking suspicious activity.

2. **Robotics and Autonomous Systems**:
   - **Use Case**: Enable a robot to follow a person in dynamic environments, such as homes or public spaces.
   - **Example**: A service robot in a hospital can use this system to follow a doctor or nurse while carrying medical supplies, adjusting its path based on the person's movements, enhancing efficiency in busy environments.

3. **Photography and Videography**:
   - **Use Case**: Keep a subject in frame during video recording or photography, even as they move.
   - **Example**: A content creator filming a vlog can mount their camera on a motorized tripod controlled by this system. As they walk or move, the camera automatically rotates to keep them centered, ensuring smooth, professional-quality footage without a dedicated camera operator.

4. **Interactive Installations**:
   - **Use Case**: Create interactive experiences in museums, exhibitions, or retail environments.
   - **Example**: In a museum, the system can control a spotlight or display screen that follows a visitor as they move through an exhibit, providing personalized information or highlighting specific artifacts based on their position.

5. **Assistive Technology**:
   - **Use Case**: Support individuals with mobility challenges by enabling devices to track and assist them.
   - **Example**: A motorized wheelchair accessory could use this system to automatically orient a camera or sensor toward a caregiver, ensuring constant visual contact for communication or monitoring purposes.

6. **Education and Research**:
   - **Use Case**: Serve as a learning tool for students and researchers exploring computer vision and IoT integration.
   - **Example**: In a university lab, students can use this project to study real-time object detection and motor control, modifying the code to experiment with different tracking algorithms or hardware configurations.

7. **Retail and Customer Engagement**:
   - **Use Case**: Enhance customer experiences in stores by tracking and engaging with shoppers.
   - **Example**: A retail store could use the system to control a display screen that follows a customer, showing personalized promotions or product information as they move through different sections of the store.

These applications demonstrate the system's flexibility, making it suitable for both hobbyist projects and professional deployments. Its open-source nature allows developers to customize it for specific needs, such as adjusting the motor type, adding new detection classes, or integrating with other hardware.

## Idea and Motivation
The motivation behind this project was to create an affordable, open-source person-tracking system that seamlessly integrates computer vision with hardware control. By leveraging YOLOv8's robust object detection capabilities and Arduino's reliable motor control, the project aims to provide a practical example of combining AI with IoT. The system is designed to be accessible to hobbyists, students, and professionals, enabling them to build and experiment with real-time tracking solutions.

## Features
- **Real-time person detection**: Uses YOLOv8 to detect people in a webcam feed with high accuracy.
- **Motor control**: Controls a DC motor via Arduino to rotate left, right, or stop based on the person's position.
- **Visual feedback**: Displays the video feed with bounding boxes and confidence scores around detected people.
- **Simple communication**: Uses serial communication to send commands from the Python script to the Arduino.

## Requirements
### Hardware
- Webcam (USB or built-in)
- Arduino board (e.g., Arduino Uno)
- DC motor with a motor driver (e.g., L298N)
- Jumper wires and a power source for the motor
- Computer with USB ports for Arduino and webcam

### Software
- Python 3.7+
- Libraries: `opencv-python`, `ultralytics`, `pyserial`, `torch`
- Arduino IDE for uploading the motor control code
- YOLOv8 model weights (`yolov8.pt`)

## Installation
1. **Set up the hardware**:
   - Connect the DC motor to the motor driver (e.g., L298N).
   - Connect the motor driver pins to the Arduino:
     - `ENB` to PWM pin 9
     - `IN3` to digital pin 8
     - `IN4` to digital pin 7
   - Power the motor driver and Arduino appropriately.
   - Connect the webcam to your computer.

2. **Install Python dependencies**:
   ```bash
   pip install opencv-python ultralytics pyserial torch
   ```
   Download the YOLOv8 model weights (`yolov8.pt`) from the Ultralytics website or use the pre-trained model provided by the library.

3. **Upload Arduino code**:
   - Open `motor_control.ino` in the Arduino IDE.
   - Upload the code to your Arduino board.

4. **Run the Python script**:
   - Update the serial port in `main.py` (e.g., `COM4` to match your Arduino's port).
   - Run the script:
     ```bash
     python main.py
     ```

## How It Works
1. **Video Capture**: The Python script captures video from the webcam at 640x480 resolution.
2. **Person Detection**: The YOLOv8 model processes each frame to detect people, with a confidence threshold of 0.5 and IoU of 0.7.
3. **Position Analysis**:
   - The script calculates the center of the detected person's bounding box.
   - If the person is too far left (`center_x < FRAME_WIDTH/2 - CENTER_THRESHOLD`), it sends an 'L' command to move the motor left.
   - If the person is too far right (`center_x > FRAME_WIDTH/2 + CENTER_THRESHOLD`), it sends an 'R' command to move the motor right.
   - If the person is centered or no person is detected, it sends an 'S' command to stop the motor.
4. **Motor Control**: The Arduino receives serial commands ('L', 'R', 'S') and controls the motor accordingly:
   - 'L': Rotates the motor left.
   - 'R': Rotates the motor right.
   - 'S': Stops the motor.
5. **Visual Output**: The video feed is displayed with bounding boxes and confidence scores for detected people.

## Usage
1. Ensure all hardware is connected and powered.
2. Run the Python script (`main.py`).
3. The webcam feed will appear, showing detected people with bounding boxes.
4. The motor will rotate to keep the person centered in the frame.
5. Press `q` to stop the program.

## Troubleshooting
- **Camera not working**: Ensure the webcam is connected and the correct camera index (e.g., 0) is used in `cv2.VideoCapture(0)`.
- **Arduino not responding**: Verify the correct serial port and baud rate (9600). Check the Arduino IDE's Serial Monitor for debugging.
- **YOLO model issues**: Ensure `yolov8.pt` is in the same directory as `main.py` or specify the correct path.
- **Motor not moving**: Check motor driver connections and power supply. Ensure the motor driver is compatible with your motor.

## Future Improvements
- Add support for multiple people tracking (e.g., track the closest person).
- Implement PID control for smoother motor movements.
- Add a GUI for easier configuration of thresholds and model parameters.
- Support different motor types or servos for more precise control.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Acknowledgments
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) for the YOLOv8 model.
- [OpenCV](https://opencv.org/) for video processing.
- [Arduino](https://www.arduino.cc/) for motor control.