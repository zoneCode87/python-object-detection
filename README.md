# Python Object Detection 🎯

This project demonstrates real-time object detection using a pre-trained **SSD MobileNet V3 Large model** with **OpenCV** in Python. It's designed to identify and classify objects within video streams or images based on the **COCO dataset**.


## **About The Project**

This project leverages the power of deep learning for object detection. It utilizes a pre-trained `ssd_mobilenet_v3_large_coco_2020_01_14` model (frozen inference graph) to perform efficient and accurate object recognition. The project is built with **Python 3.8** and relies heavily on the **OpenCV** library for image and video processing. The model is trained on the extensive **COCO dataset**, allowing it to detect a wide variety of common objects.

---

## **Features**

* **Real-time Object Detection**: Detects objects in live video streams from your webcam.
* **Pre-trained Model**: Uses the `SSD MobileNet V3 Large` model for out-of-the-box detection capabilities.
* **COCO Dataset Support**: Recognizes objects from the 80 classes of the COCO dataset.
* **Simple to Use**: Easy setup and execution.

---
## **Getting Started**

To get a local copy up and running, follow these simple steps.

### **Prerequisites**
Ensure you have **Python 3.8** installed on your system. You can check your Pyth

# **Installation**

1.Clone the repository:
https://github.com/lihini223/Object-Detection-model.git

2.Navigate into the project directory:
cd Python-Object-Detection

Virtual Environment Setup
It's highly recommended to set up a virtual environment to manage project dependencies.
python -m venv venv

Activate the virtual environment:
On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install the required Python packages
pip install opencv-python pyttsx3


Usage
Once you have set up the environment and installed the dependencies, you can run the object detection script.

To start the object detection:
python main.py

This will open your webcam feed, and the detected objects will be highlighted with bounding boxes and labels.