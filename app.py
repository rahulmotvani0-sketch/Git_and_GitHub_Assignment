import os
import json
from datetime import datetime
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['todo_db']
todos_collection = db['todos']

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

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    """Backend route created in master_2 that accepts itemName and itemDescription via POST and stores them in MongoDB."""
    req_data = request.get_json(silent=True) or request.form.to_dict()
    
    item_name = req_data.get('itemName')
    item_desc = req_data.get('itemDescription', '')
    
    if not item_name:
        return jsonify({
            'status': 'error',
            'message': 'itemName is required'
        }), 400
        
    todo_document = {
        'itemName': item_name,
        'itemDescription': item_desc,
        'createdAt': datetime.utcnow().isoformat(),
        'sourceBranch': 'master_2'
    }
    
    result = todos_collection.insert_one(todo_document)
    
    return jsonify({
        'status': 'success',
        'message': 'To-Do item successfully stored in MongoDB',
        'id': str(result.inserted_id),
        'data': {
            'itemName': item_name,
            'itemDescription': item_desc
        }
    }), 201

@app.route('/api/todos', methods=['GET'])
def get_all_todos():
    """Helper endpoint to fetch all stored MongoDB To-Do items."""
    records = []
    for doc in todos_collection.find().sort('_id', -1):
        records.append({
            'id': str(doc['_id']),
            'itemName': doc.get('itemName', ''),
            'itemDescription': doc.get('itemDescription', ''),
            'itemId': doc.get('itemId', ''),
            'itemUuid': doc.get('itemUuid', ''),
            'itemHash': doc.get('itemHash', ''),
            'createdAt': doc.get('createdAt', '')
        })
    return jsonify({
        'status': 'success',
        'count': len(records),
        'todos': records
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
