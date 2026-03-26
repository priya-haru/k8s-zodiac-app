from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>K8s Zodiac v3</title>
    <style>
        body { background: #0f0c29; color: #00d2ff; text-align: center; font-family: 'Segoe UI', sans-serif; padding-top: 80px; }
        .box { background: rgba(255,255,255,0.1); padding: 40px; border-radius: 20px; display: inline-block; border: 1px solid #00d2ff; box-shadow: 0 0 20px #00d2ff; }
        input { padding: 10px; margin: 10px; width: 60px; border-radius: 5px; border: none; }
        button { padding: 10px 20px; background: #00d2ff; color: #0f0c29; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
        #res { margin-top: 20px; font-size: 28px; color: #f1c40f; text-shadow: 2px 2px #000; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🌌 Cosmos Zodiac v3 🌌</h1>
        <p>Enter your birth details:</p>
        <input type="number" id="d" placeholder="Day">
        <input type="number" id="m" placeholder="Month">
        <br>
        <button onclick="go()">Read My Fate</button>
        <div id="res"></div>
    </div>
    <script>
        async function go(){
            const r = await fetch('/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({day: document.getElementById('d').value, month: document.getElementById('m').value})
            });
            const data = await r.json();
            document.getElementById('res').innerText = "Your Sign: " + data.zodiac_sign;
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
    d, m = int(data.get('day')), int(data.get('month'))
    if (m == 1 and d >= 20) or (m == 2 and d <= 18): sign = "Aquarius"
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20): sign = "Pisces"
    elif (m == 3 and d >= 21) or (m == 4 and d <= 19): sign = "Aries"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): sign = "Taurus"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): sign = "Gemini"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): sign = "Cancer"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): sign = "Leo"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): sign = "Virgo"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): sign = "Libra"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21): sign = "Scorpio"
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21): sign = "Sagittarius"
    else: sign = "Capricorn"
    return jsonify({"zodiac_sign": sign})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
