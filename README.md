# 🎨 Air Canvas Project

A Virtual Air Canvas that allows users to draw on screen using hand gestures or a colored pointer detected through a webcam.


## 🚀 Features

- ✍️ Draw in air using a pointer
- 🎨 Select multiple colors (Blue, Green, Red, Yellow)
- 🧽 Clear canvas option
- 📷 Real-time webcam tracking
- 🖥️ Simple and interactive UI


## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy


## 📂 Project Structure

Air-Canvas/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│── assets/
│     └── demo.png


## ⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com//air-canvas.git
cd air-canvas
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
python main.py


## 🎯 How It Works
The webcam captures live video.
A colored object (or finger) is detected.
The position of the object is tracked.
Based on position:
Top area → Select color 🎨
Drawing area → Draw ✍️
Clear button → Erase 🧽


## 🕹️ Controls
Action	Function
Move pointer to top	Select color
Move pointer below	Draw
Move to CLEAR	Clear screen
Press ESC or q	Exit


## 📸 Output
🖥️ Drawing Interface

<img width="797" height="635" alt="Screenshot 2026-04-08 151146" src="https://github.com/user-attachments/assets/5a08de3e-6bd2-43a0-b181-e635348d0122" />
