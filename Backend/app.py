from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api/dashboard")
def get_dashboard():
    with open("dashboard_data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)