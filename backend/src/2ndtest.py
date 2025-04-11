# flask_station_api/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from mta_api import *

app = Flask(__name__)
CORS(app)  # Allow mobile and web apps to access this server

# Dummy data for NYC subway stations with accessibility info
stations_data = [
    {"name": "Times Square - 42 St", "elevator": True, "escalator": True},
    {"name": "34 St - Penn Station", "elevator": True, "escalator": False},
    {"name": "14 St - Union Square", "elevator": False, "escalator": True},
    {"name": "Canal St", "elevator": False, "escalator": False}
]

letters = ['a', 'b', 'c', 'd', '1']

testData = [{
  "type":"Elevator",
  "reason":"Power Outage",
  "outage_date": "10/24/2006",
  "return_serice": "10/24/2026",
  "service_area": "idk"
}, {
  "type":"Elevator",
  "reason":"Power Outage",
  "outage_date": "10/24/2006",
  "return_serice": "10/24/2026",
  "service_area": "idk"
}]

@app.route('/api/stations', methods=['GET'])
def get_stations_A():
    return mta_api.nearest_station(), 200

@app.route('/api/lines/<string:station_name>', methods=['GET'])
def get_station_lines(station_name):
    # TODO Retrieve the Lines from this station
    return jsonify(letters), 200

@app.route('/api/outages/<string:station_name>', methods=['GET'])
def get_outages(station_name):
    # TODO Retrieve the Outages on each station
    return jsonify(testData), 200

#TODO determine and provide additional routes
if __name__ == '__main__':
    app.run(debug=True)
