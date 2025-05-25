# Real-Time Object Detection with Python 🎯  

![Demo 1](/img/img1.PNG) | ![Demo 2](/img/img2.PNG)  
:-------------------------:|:-------------------------:
![Demo 3](/img/img3.PNG) | ![Demo 4](/img/img4.PNG)  

A lightweight object detection system using **OpenCV** and **SSD MobileNet V3** to identify 80 common objects from the COCO dataset in real-time.

---

## ✨ Features  
✔ **Live Camera Detection** - Works with webcams or video files  
✔ **Pre-trained Model** - SSD MobileNet V3 (optimized for speed/accuracy balance)  
✔ **Voice Feedback** - Optional text-to-speech with `pyttsx3`  
✔ **Threshold Control** - Adjustable confidence level for detections  

---

## ⚙️ Installation  

### Requirements  
- Python 3.8 !important 

### Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/lihini223/Object-Detection-model.git
   cd Object-Detection-model

2. Set up virtual environment::  
   ```bash
    python -m venv env

3. Activate environment
   ```bash
    # Windows
    .\env\Scripts\activate
    # Mac/Linux
    source env/bin/activate

4. Install dependencies:
    ```bash
     pip install opencv-python pyttsx3 

5. Usage 
    ```bash
    python main.py
    press Q to quit
