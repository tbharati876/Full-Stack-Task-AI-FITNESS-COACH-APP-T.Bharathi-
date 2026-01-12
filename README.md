Google Colab Workspace Link: https://colab.research.google.com/drive/1ZlFkiwPTS86aG88_BDIJMyEbPRoJKj_8?usp=sharing

Video Demo URL: https://drive.google.com/file/d/1eLD8kkhLbdsxpp_NbeRkT3Kh_VCg2z32/view?usp=drivesdk

🏋️ AI Fitness Coach
A lightweight, full-stack AI Fitness application that generates personalized workout and nutrition plans based on user input. It features a Tailwind CSS interface, a Flask backend, and built-in Text-to-Speech (TTS) capabilities so users can listen to their plans.

Features
Personalized Logic: Tailors workout intensity and diet recommendations based on Age, Goal (Muscle Gain vs. Weight Loss), and Dietary preferences.

Voice Integration: Uses the Web Speech API to read the generated fitness plan aloud.

Modern UI: Styled with Tailwind CSS in a dark-themed, "stealth" aesthetic.

Instant Deployment: Configured to run in Google Colab or local environments using PyNgrok for instant public URL tunneling.

🛠️ Tech Stack
Frontend: HTML5, JavaScript (ES6+), Tailwind CSS.

Backend: Python, Flask, Flask-CORS.

Tunneling: PyNgrok (exposes local server to the web).

Speech: Web Speech Synthesis API.

Getting Started
1. Prerequisites
You will need an Ngrok Auth Token to expose the app to the web.

Sign up at ngrok.com.

Copy the token from the dashboard.

2. Installation & Setup

Bash

pip install flask flask-cors pyngrok
3. Configuration
Replace the NGROK_TOKEN variable in the code with actual token:

Python

NGROK_TOKEN = "YOUR_NGROK_AUTH_TOKEN_HERE"
4. Running the App
Run the script in  Colab cell:

Bash

python app.py
The console will output a Public URL (e.g., https://xxxx-xxx.ngrok-free.app). Click it to access coach!

How It Works
Input: User enters their age, selects a fitness goal, and chooses a diet type.

Request: The frontend sends a POST request to the /api/generate endpoint.

Logic: The Python backend processes the data and returns a structured string containing workout sets, exercises, and meal suggestions.

Display & Audio: The frontend renders the plan and enables the "Listen" button for auditory feedback.
