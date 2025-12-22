!pip install flask flask-cors pyngrok -q

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import threading

NGROK_TOKEN = "36mSHpSl4DWk4VZO6zTudKO3Piz_2ReYvKNYAz8zPKgUJRMxH" 

app = Flask(__name__)
CORS(app)

# BACKEND LOGIC
def generate_fitness_logic(data):
    goal = data.get('goal', 'Fitness')
    diet = data.get('diet', 'Standard')
    age = data.get('age', '25')
    
    plan = f"=== {goal.upper()} PLAN FOR AGE {age} ===\n\n"
    
    if "Gain" in goal:
        plan += "WORKOUT: Focus on Compound Lifts like Squats, Deadlifts, and Bench Press.\n"
        plan += "SETS: 4 Sets of 8 to 10 reps with 90 seconds rest.\n"
    else:
        plan += "WORKOUT: High-Intensity Interval Training and Steady Cardio.\n"
        plan += "SETS: 3 Sets of 15 to 20 reps with 30 seconds rest.\n"
        
    plan += f"\nDIET ({diet}):\n"
    if diet == "Veg":
        plan += "- Breakfast: Paneer bhurji or Oats.\n- Lunch: Dal, Brown Rice, and Broccoli.\n"
    else:
        plan += "- Breakfast: Eggs and Avocado toast.\n- Lunch: Grilled Chicken or Fish with Sweet Potato.\n"
    
    plan += "\nTIP: Drink 3 liters of water daily and sleep 8 hours."
    return plan

# FRONTEND HTML 
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Fitness Coach</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-black text-white p-10">
    <div class="max-w-xl mx-auto border border-gray-800 p-8 rounded-2xl bg-gray-900 shadow-2xl">
        <h1 class="text-3xl font-bold text-blue-500 mb-6 text-center uppercase tracking-tight">AI Fitness Coach</h1>
        
        <div class="space-y-4">
            <input id="age" type="number" placeholder="Age" class="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg outline-none focus:border-blue-500">
            <select id="goal" class="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg outline-none focus:border-blue-500">
                <option value="Muscle Gain">Muscle Gain</option>
                <option value="Weight Loss">Weight Loss</option>
            </select>
            <select id="diet" class="w-full p-3 bg-gray-800 border border-gray-700 rounded-lg outline-none focus:border-blue-500">
                <option value="Veg">Vegetarian</option>
                <option value="Non-Veg">Non-Vegetarian</option>
            </select>
            <button onclick="run()" id="btn" class="w-full bg-blue-600 p-3 rounded-lg font-bold hover:bg-blue-500 transition shadow-lg">Generate Plan</button>
        </div>

        <div id="resultBox" class="mt-8 hidden p-6 bg-gray-800 rounded-lg border-l-4 border-blue-500 relative">
            <div class="flex justify-between items-center mb-4">
                <h2 class="text-blue-400 font-bold uppercase text-sm">Your Personalized Plan</h2>
                <button onclick="speakPlan()" class="bg-gray-700 hover:bg-gray-600 text-white px-3 py-1 rounded-md text-xs transition flex items-center gap-2">
                    <span>🔊</span> Listen
                </button>
            </div>
            <pre id="output" class="whitespace-pre-wrap text-sm text-gray-300 leading-relaxed"></pre>
        </div>
    </div>

    <script>
        let lastGeneratedPlan = "";

        async function run() {
            const btn = document.getElementById('btn');
            btn.innerText = "Processing...";
            
            const payload = {
                age: document.getElementById('age').value,
                goal: document.getElementById('goal').value,
                diet: document.getElementById('diet').value
            };

            try {
                const res = await fetch(window.location.origin + '/api/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                
                lastGeneratedPlan = data.plan; // Store for voice
                document.getElementById('resultBox').classList.remove('hidden');
                document.getElementById('output').innerText = data.plan;
                
            } catch (e) {
                alert("Connection Error: Make sure to use the Ngrok URL, not localhost.");
            } finally {
                btn.innerText = "Generate Plan";
            }
        }

        function speakPlan() {
            if ('speechSynthesis' in window) {
                // Stop any current speech
                window.speechSynthesis.cancel();
                
                const utterance = new SpeechSynthesisUtterance(lastGeneratedPlan);
                utterance.pitch = 1;
                utterance.rate = 0.95; // Slightly slower for clarity
                utterance.volume = 1;
                
                window.speechSynthesis.speak(utterance);
            } else {
                alert("Sorry, your browser does not support voice features.");
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML_TEMPLATE

@app.route('/api/generate', methods=['POST'])
def handle_request():
    return jsonify({"plan": generate_fitness_logic(request.json)})

# SERVER & NGROK
def start_server():
    app.run(port=5000, use_reloader=False)

if __name__ == "__main__":
    ngrok.kill() 
    ngrok.set_auth_token(NGROK_TOKEN)
    public_url = ngrok.connect(5000).public_url
    print(f"\n🚀 APP LIVE AT: {public_url}\n")
    
    threading.Thread(target=start_server).start()
