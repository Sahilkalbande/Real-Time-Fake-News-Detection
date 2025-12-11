from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    
    result = {
        'verdict': random.choice(['Real', 'Fake']),
        'confidence': random.randint(70, 95),
        'indicators': [
            {'label': 'Source Credibility', 'score': random.randint(70, 95)},
            {'label': 'Content Analysis', 'score': random.randint(70, 95)},
            {'label': 'Language Pattern', 'score': random.randint(70, 95)},
            {'label': 'Fact Verification', 'score': random.randint(70, 95)}
        ]
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)