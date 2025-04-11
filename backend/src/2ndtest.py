# flask_station_api/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from mta_api import *
from urllib.parse import unquote

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

mta = mta_api()

@app.route('/api/stations', methods=['GET'])
def get_stations_A():
    try: 
        # data = request.get_json()
        # latitude = data.get('latitude')
        # longitude = data.get('longitude')
    # Code that might raise an exception
        return mta.remove_duplicates(mta.nearest_station(40.76955871435315, -73.98221834841239))[:5], 200
    except Exception as e:
    # Catch any other exception
        print(f"An unexpected error occurred: {e}")
    return jsonify(""), 404
@app.route('/api/lines/<string:station_id>', methods=['GET'])
def get_station_lines(station_id):
    print(station_id)
    # TODO Retrieve the Lines from this station
    print(mta.station_lines(station_id))
    return mta.station_lines(station_id), 200

@app.route('/api/outages/<string:station_name>', methods=['GET'])
def get_outages(station_name):
    station_name_spaces = unquote(station_name)
    # TODO Retrieve the Outages on each station
    print(mta.accessible(station_name_spaces))
    return mta.stations_down_equpiment(station_name_spaces), 200

#TODO determine and provide additional routes
if __name__ == '__main__':
    app.run(debug=True)
