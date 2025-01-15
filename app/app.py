from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Welcome to Docker Compose Demo!"})

@app.route('/db')
def db_connection():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="rootpassword",
            database="demo"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        return jsonify({"message": f"Connected to database: {db_name}"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
