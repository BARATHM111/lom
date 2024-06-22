from flask import Flask, render_template, request, jsonify
import mysql.connector
import json
import requests
from datetime import date, datetime

app = Flask(__name__)

# Replace with your updated AI model API key and endpoint
API_KEY = 'pk-gydFkPtuNbLLolXEJxxgTkXFiWMOggZCYVcwrfCUpuJpGWNq'
MODEL_ENDPOINT = 'https://api.pawan.krd/v1/chat/completions'

# Custom JSON encoder to handle datetime objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    host = data.get('host')
    user = data.get('user')
    password = data.get('password')

    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES")
        databases = [db[0] for db in cursor.fetchall()]
        conn.close()
        return jsonify({'status': 'success', 'databases': databases})
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    host = data.get('host')
    user = data.get('user')
    password = data.get('password')
    database = data.get('database')
    user_query = data.get('query')

    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        db_json = {}
        for table in tables:
            table_name = table['Tables_in_' + database] if 'Tables_in_' + database in table else next(iter(table.values()))
            cursor.execute(f"SELECT * FROM {table_name}")
            table_data = cursor.fetchall()

            # Convert datetime objects to ISO format
            for row in table_data:
                for key, value in row.items():
                    if isinstance(value, (date, datetime)):
                        row[key] = value.isoformat()

            db_json[table_name] = table_data

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            "model": "pai-001",
            "messages": [
                {"role": "system", "content": "You are an assistant that answers questions based on the provided database."},
                {"role": "user", "content": f"Database: {json.dumps(db_json)}"},
                {"role": "user", "content": user_query}
            ]
        }

        response = requests.post(MODEL_ENDPOINT, headers=headers, json=payload)
        result = response.json()

        conn.close()

        # Extract the answer from the model response
        answer = result['choices'][0]['message']['content'].strip()

        return jsonify({'status': 'success', 'response': answer})
    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})
    except requests.RequestException as err:
        return jsonify({'status': 'error', 'message': 'Error contacting AI model API: ' + str(err)})

if __name__ == '__main__':
    app.run(debug=True)