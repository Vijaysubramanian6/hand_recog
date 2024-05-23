# Real-time Hand Tracking and Gesture Recognition

This project uses OpenCV and MediaPipe to perform real-time hand tracking and gesture recognition via a webcam. It detects whether a hand is open or closed by calculating the distances between fingertips and their respective metacarpophalangeal (MCP) joints and displays the status on the video feed.

## Features

- Real-time hand tracking using MediaPipe
- Detection of open or closed hand gestures
- Visualization of hand landmarks on the video feed
- Displays gesture status ("Closed" or "Open") on the video feed

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/hand-gesture-recognition.git
   cd hand-gesture-recognition
   Install the required dependencies:
   sh

   ```

python hand_tracking.py
The webcam will open, and the program will start detecting and displaying hand gestures. Press q to quit the application.

## Code Overview

Initialization: The MediaPipe hands solution and drawing utilities are initialized.

Webcam Access: The script accesses the webcam feed using OpenCV.

Distance Calculation: A helper function calculates the Euclidean distance between two 3D points.

Gesture Detection: The is_hand_closed function determines if the hand is closed by comparing the distances between fingertips and their respective MCP joints to a threshold.

Main Loop: Captures frames from the webcam, processes them to detect hands, draws hand landmarks, checks the hand gesture, and displays the result.

# License

This project is licensed under the MIT License.
