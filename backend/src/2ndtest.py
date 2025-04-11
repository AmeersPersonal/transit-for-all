# flask_station_api/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow mobile and web apps to access this server

# Dummy data for NYC subway stations with accessibility info
stations_data = [
    {"name": "Times Square - 42 St", "elevator": True, "escalator": True},
    {"name": "34 St - Penn Station", "elevator": True, "escalator": False},
    {"name": "14 St - Union Square", "elevator": False, "escalator": True},
    {"name": "Canal St", "elevator": False, "escalator": False}
]

# @app.route('/api/stations', methods=['GET'])

@app.route('/')

def get_stations_A():
    return jsonify(stations_data)

if __name__ == '__main__':
    app.run(debug=True)
