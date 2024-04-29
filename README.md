# Eye-detection

This python script utilizes OpenCV to detect and track objects (eyes, in this case) using the device camera in real time. It uses a pre-trained object detection model to identify eyes within each frame and draws bounding boxes around them for visualization.

Instructions:
1. Ensure you have Python and OpenCV installed on your system.
2. Ensure that the system has a camera that can be used.
3. Download the Haar Cascade dataset to detect eyes imported from https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml 
4. Download the provided Python script.
5. Place the Python script and the dataset file in the same directory.
6. Run the script using the command: python detecteye.py
7. Press 'q' to exit the application.
