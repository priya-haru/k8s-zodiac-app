from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is the "Face" of your app
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>K8s Zodiac</title>
    <style>
        body { background: #1a1a2e; color: #e94560; text-align: center; font-family: 'Segoe UI', sans-serif; padding-top: 100px; }
        .box { background: #16213e; padding: 40px; border-radius: 20px; display: inline-block; border: 2px solid #0f3460; }
        input { padding: 10px; border-radius: 5px; border: none; width: 60px; margin: 10px; }
        button { padding: 10px 20px; background: #e94560; color: white; border: none; border-radius: 5px; cursor: pointer; }
        #res { margin-top: 20px; font-size: 24px; color: #f1c40f; }
    </style>
</head>
<body>
    <div class="box">
        <h1>✨ K8s Star Chart ✨</h1>
        <p>Enter Birth Date:</p>
        <input type="number" id="d" placeholder="Day">
        <input type="number" id="m" placeholder="Month">
        <br>
        <button onclick="go()">Find My Sign</button>
        <div id="res"></div>
    </div>
    <script>
        async function go(){
            const d = document.getElementById('d').value;
            const m = document.getElementById('m').value;
            const r = document.getElementById('res');
            r.innerText = "Consulting the stars...";
            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({day: d, month: m})
                });
                const data = await response.json();
                r.innerText = "Your Sign: " + data.zodiac_sign;
            } catch(e) { r.innerText = "Error connecting to API"; }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    day = int(data.get('day'))
    month = int(data.get('month'))
    # Real Zodiac Logic
    if (month == 1 and day >= 20) or (month == 2 and day <= 18): sign = "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20): sign = "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19): sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): sign = "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): sign = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): sign = "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): sign = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): sign = "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): sign = "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): sign = "Sagittarius"
    else: sign = "Capricorn"
    return jsonify({"zodiac_sign": sign})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
