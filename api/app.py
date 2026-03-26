from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>K8s Oracle v4</title>
    <style>
        body { background: #0b0d17; color: #e0e0e0; text-align: center; font-family: 'Georgia', serif; padding: 20px; }
        .container { background: rgba(20, 24, 45, 0.9); padding: 30px; border-radius: 15px; border: 1px solid #4a5568; max-width: 600px; margin: auto; box-shadow: 0 0 30px #2d3748; }
        input, select { padding: 10px; margin: 10px; border-radius: 5px; border: 1px solid #4a5568; background: #1a202c; color: white; }
        button { padding: 15px 30px; background: linear-gradient(45deg, #6b46c1, #3182ce); color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; transition: 0.3s; }
        button:hover { transform: scale(1.05); box-shadow: 0 0 15px #6b46c1; }
        .result-box { margin-top: 30px; text-align: left; line-height: 1.6; }
        .gold { color: #ecc94b; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 The K8s Oracle 🔮</h1>
        <p>Consult the digital heavens for your destiny</p>
        <input type="number" id="d" placeholder="Day (1-31)">
        <input type="number" id="m" placeholder="Month (1-12)">
        <input type="text" id="p" placeholder="City of Birth">
        <br>
        <button onclick="predict()">Unveil My Future</button>
        <div id="res" class="result-box"></div>
    </div>
    <script>
        async function predict(){
            const resDiv = document.getElementById('res');
            resDiv.innerHTML = "<i>The spirits are calculating...</i>";
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    day: document.getElementById('d').value, 
                    month: document.getElementById('m').value,
                    place: document.getElementById('p').value
                })
            });
            const data = await response.json();
            resDiv.innerHTML = `
                <p><span class="gold">Sign:</span> ${data.zodiac_sign}</p>
                <p><span class="gold">Career Path:</span> ${data.career}</p>
                <p><span class="gold">Love Match:</span> ${data.match}</p>
                <p><span class="gold">Prediction:</span> ${data.prediction}</p>
                <p><i>Born in: ${data.place_received}</i></p>
            `;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML_PAGE)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    d, m = int(data.get('day')), int(data.get('month'))
    place = data.get('place', 'The Unknown')
    
    # Sign Logic
    if (m == 1 and d >= 20) or (m == 2 and d <= 18): sign, career, match = "Aquarius", "Technology/Innovation", "Leo"
    elif (m == 2 and d >= 19) or (m == 3 and d <= 20): sign, career, match = "Pisces", "Arts/Music", "Virgo"
    elif (m == 3 and d >= 21) or (m == 4 and d <= 19): sign, career, match = "Aries", "Leadership/Entrepreneurship", "Libra"
    elif (m == 4 and d >= 20) or (m == 5 and d <= 20): sign, career, match = "Taurus", "Finance/Nature", "Scorpio"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 20): sign, career, match = "Gemini", "Journalism/Communication", "Sagittarius"
    elif (m == 6 and d >= 21) or (m == 7 and d <= 22): sign, career, match = "Cancer", "Healthcare/Psychology", "Capricorn"
    elif (m == 7 and d >= 23) or (m == 8 and d <= 22): sign, career, match = "Leo", "Entertainment/Politics", "Aquarius"
    elif (m == 8 and d >= 23) or (m == 9 and d <= 22): sign, career, match = "Virgo", "Engineering/Science", "Pisces"
    elif (m == 9 and d >= 23) or (m == 10 and d <= 22): sign, career, match = "Libra", "Law/Design", "Aries"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 21): sign, career, match = "Scorpio", "Investigation/Strategy", "Taurus"
    elif (m == 11 and d >= 22) or (m == 12 and d <= 21): sign, career, match = "Sagittarius", "Travel/Philosophy", "Gemini"
    else: sign, career, match = "Capricorn", "Management/Architecture", "Cancer"

    predictions = [
        "A major Kubernetes success is coming your way.",
        "A hidden opportunity in your network will reveal itself today.",
        "Your hard work will soon pay off in unexpected ways.",
        "Avoid unnecessary cloud costs; stay grounded.",
        "The stars suggest a breakthrough in your current project."
    ]

    return jsonify({
        "zodiac_sign": sign,
        "career": career,
        "match": match,
        "prediction": random.choice(predictions),
        "place_received": place
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
