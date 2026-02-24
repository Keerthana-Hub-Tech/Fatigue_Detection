

---

#  Cognitive Fatigue Detection System

### Real-Time Fatigue Detection using Typing & Mouse Dynamics

##  Overview

This project is a **Machine Learning–based Cognitive Fatigue Detection System** that predicts a user’s mental state based on typing behavior and mouse movement patterns.

The system analyzes behavioral biometrics in real time and classifies the user into:

* **Fresh**
* **Mild**
* **Fatigue**

The model is deployed as a **Flask web application** and can be hosted on cloud platforms like Render.

---

##  Features

*  Real-time typing analysis (1-minute session)
*  Mouse movement tracking
*  Behavioral feature extraction
*  Random Forest ML model
*  Flask web interface


---

##  Features Used for Prediction

The model is trained on the following behavioral features:

| Feature            | Description                                 |
| ------------------ | ------------------------------------------- |
| `avg_key_interval` | Average time between consecutive keystrokes |
| `typing_speed`     | Words per minute (WPM)                      |
| `backspace_rate`   | Backspaces per minute                       |
| `avg_mouse_speed`  | Average mouse movement speed                |

These features are calculated in real-time in the browser and sent to the backend for prediction.

---

##  Model Details

* Algorithm: **Random Forest Classifier**
* Accuracy (on dataset): **100%**
* Model saved using: `pickle`
* Input: 4 behavioral features
* Output: Fatigue classification label



---

##  Dataset Collection

The dataset was collected using a custom Python script that tracks:

* Keyboard events using `pynput`
* Mouse movement behavior
* Session-based labeling (Fresh, Mild, Fatigued)
* 60-second behavior windows

Statistical balancing and augmentation were applied before training.

---

##  Use Cases

* Student productivity monitoring
* Workplace fatigue detection
* Driver attention systems
* Behavioral biometric research
* Human-computer interaction studies
  
Live at :https://fatigue-detection-l6d1.onrender.com
---

##  Note

This project is for **research and academic purposes** only.
It does not collect or store personal textual content — only behavioral timing metrics.

---

##  Author

**Keerthana V.**
B.Tech CSE (IoT)
Passionate about AI, Behavioral Analytics & Intelligent Systems

---


