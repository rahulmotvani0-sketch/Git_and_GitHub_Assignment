import os
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'items.json')

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"error": "Data file not found"}

@app.route('/')
def home():
    data = load_data()
    return render_template('index.html', data=data)

@app.route('/api')
def api():
    """Serves the JSON file contents as requested in Task 1 & 2."""
    data = load_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
