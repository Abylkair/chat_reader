from flask import Flask, jsonify, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages')
def get_messages():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    # Execute the query to the database, ordering by time
    cursor.execute("SELECT id, name, message, timestamp, 'user' AS type FROM user_messages "
                   "UNION ALL "
                   "SELECT id, name, message, timestamp, 'bot' AS type FROM bot_messages "
                   "ORDER BY timestamp ASC")

    # Fetch the query results
    rows = cursor.fetchall()

    # Convert the results into a list of dictionaries
    messages_list = []
    for row in rows:
        message_dict = {
            'id': row[0],
            'name': row[1],
            'message': row[2],
            'timestamp': row[3].strftime('%Y-%m-%d %H:%M:%S') if row[3] else None,
            'type': row[4]
        }
        messages_list.append(message_dict)

    conn.close()

    return jsonify(messages_list)

@app.route('/messages/<int:user_id>')
def get_user_messages(user_id):
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    # Execute the query to the database, ordering by time
    cursor.execute("SELECT id, name, message, timestamp, 'user' AS type FROM user_messages WHERE id = %s "
                   "UNION ALL "
                   "SELECT id, name, message, timestamp, 'bot' AS type FROM bot_messages WHERE id = %s "
                   "ORDER BY timestamp ASC",
                   (user_id, user_id))

    # Fetch the query results
    rows = cursor.fetchall()

    # Convert the results into a list of dictionaries
    messages_list = []
    for row in rows:
        message_dict = {
            'id': row[0],
            'name': row[1],
            'message': row[2],
            'timestamp': row[3].strftime('%Y-%m-%d %H:%M:%S') if row[3] else None,
            'type': row[4]
        }
        messages_list.append(message_dict)

    conn.close()

    return jsonify(messages_list)

if __name__ == '__main__':
    app.run(debug=True)
