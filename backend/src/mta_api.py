
import re
from urllib import response
import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format, text_format, message
import time 
import pandas as pd


from geopy.geocoders import Nominatim

from math import radians, sin, cos, sqrt, atan2


class mta_api():

    def __init__(self):
        load_dotenv()
        self.feeds = {
            "ACE": os.environ.get("ACESr"),
            "BDFM": os.environ.get("BDFMSf"),
            "G": os.environ.get("G"),
            "JZ": os.environ.get("JZ"),
            "NQRW": os.environ.get("NQRW"),
            "L": os.environ.get("L"),
            "1234567S": os.environ.get("num_1234567S"),
            "SIR": os.environ.get("SIR")
        }
        
        self.sessions =requests.Session()

    
    
    def get_user_coordinate(self):
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode("") # Empty string gets the current location

        if location:
            print("Latitude:", location.latitude)
            print("Longitude:", location.longitude)
        else:
            print("Location not found")
                     
    def get_station_coordinate(self, stop_id):
        f= pd.read_csv("backend/src/mta_info/stops.txt")
        result = f[f["stop_id"] == stop_id]
        if not result.empty:
            lat = result.iloc[0]["stop_lat"]
            lon = result.iloc[0]["stop_lon"]

            return (float(lat), float(lon))
        else:
            return 

    def stop_id_to_long_name(self, stop_id):
        f= pd.read_csv("backend/src/mta_info/stops.txt")
        result = f[f["stop_id"] == stop_id]
        
        if not result.empty:
            stop_name = result.iloc[0]["stop_name"]
            return stop_name
        else:
            return 
    def long_name_to_id(self, name):
        f= pd.read_csv("backend/src/mta_info/stops.txt")
        result = f[f["stop_name"] == name]
        
        if not result.empty:
            stop_id = result.iloc[0]["stop_id"]
            return stop_id
        else:
            return      
        
    def long_name_to_ids(self, name):
        f = pd.read_csv("backend/src/mta_info/stops.txt")

        # Filter all rows where stop_name matches (case-insensitive for flexibility)
        result = f[f["stop_name"].str.lower() == name.lower()]

        # Get all unique stop_ids associated with that stop name
        ids = result["stop_id"].unique().tolist()

        return ids        


    def get_train_line_data(self, line):
        feed = gtfs_realtime_pb2.FeedMessage()
        key = next((k for k, v in self.feeds.items() if line in k), None)
        data = []
        response = self.sessions.get(self.feeds.get(key))

        if response.status_code != 200:
            raise Exception(f"Failed to get GTFS data: {response.status_code} - {response.text}")

        feed.ParseFromString(response.content)
        for entity in feed.entity:
            if entity.HasField("trip_update"):
                route_id= entity.trip_update.trip.route_id
                if route_id == line:
                    data.append(entity)
                
        return data


       
    


    # Load GTFS files
    

    def get_train_stops(self, train_short_name):
        routes = pd.read_csv("backend/src/mta_info/routes.txt")
        trips = pd.read_csv("backend/src/mta_info/trips.txt")
        stop_times = pd.read_csv("backend/src/mta_info/stop_times.txt")
        stops = pd.read_csv("backend/src/mta_info/stops.txt")
        # 1. Get route_id for the N train
        route_ids = routes[routes["route_short_name"] == train_short_name]["route_id"]
    
        if route_ids.empty:
            return []

        route_id = route_ids.iloc[0]

        # 2. Get trips for the N train
        train_trips = trips[trips["route_id"] == route_id]

        # 3. Pick the most complete trip (has the most stops)
        most_common_trip = (
            stop_times[stop_times["trip_id"].isin(train_trips["trip_id"])]
            .trip_id.value_counts()
            .idxmax()
        )

        # 4. Get ordered stop_ids for that trip
        ordered_stops = (
            stop_times[stop_times["trip_id"] == most_common_trip]
            .sort_values("stop_sequence")["stop_id"]
            .tolist()
        )

        # 5. Get stop names from stops.txt
        stop_info = stops[stops["stop_id"].isin(ordered_stops)][["stop_id", "stop_name"]]

        # Ensure order is preserved
        stop_info["order"] = stop_info["stop_id"].apply(lambda x: ordered_stops.index(x))
        stop_info = stop_info.sort_values("order")

        return stop_info[["stop_id", "stop_name"]].to_dict(orient="records")


        


    def nearest_station(self, user_lat, user_lon):
        f = pd.read_csv("backend/src/mta_info/stops.txt")
        
        stations = []
        
        for _, row in f.iterrows():
            stop_lat = row["stop_lat"]
            stop_lon = row["stop_lon"]
            stop_id = row["stop_id"]
  
            lat = (user_lat -(stop_lat))**2
            lon =(user_lon-(stop_lon))**2
            distance = sqrt(lat+lon)
            
            stations.append({
                "stop_id": stop_id,
                "stop_name": row["stop_name"],
                "distance": distance
            })

        sorted_data = sorted(stations, key=lambda s: s["distance"])
        return sorted_data  # top 5 nearest stations

    def remove_duplicates(self, stations):
        seen = set()
        unique_stations = []

        for station in stations:
            if (station['stop_name'] not in seen):
                unique_stations.append(station)
                seen.add(station['stop_name'])

        return unique_stations

    def is_station_accessible(self, station_name):
        url ="https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json"
        response  = requests.get(url)
        data = response.json()
        for outage in data:
            if outage["station"] != station_name:
                continue
            if outage["outagedate"] is not None:
                return False
            
        return True
    
    def accessible(self, station):
        url ="https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json"
        response  = requests.get(url)
        data = response.json()
        elevator= {
            "equipment": "elevator",
            "outage":False
        }
        escalator= {
            "equipment": "escalator",
            "outage":False
        }
        for outage in data:
            if outage["station"] != station:
                return [elevator, escalator]
            if outage["outagedate"] is not None:
                if outage["equipmenttype"] == "ES":
                    escalator["outage"]==True
                if outage["equipmenttype"] == "EL":
                    elevator["outage"]==True
        t = []
        t.append(escalator)
        t.append(elevator)
        return elevator

    
    def stations_down_equpiment(self, station_name):
        equipment_outages = []
        url ="https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fnyct_ene.json"
        response  = requests.get(url)
        data = response.json()
        equipment_type=[]

        for equipment in data:
            if equipment["station"] != station_name:
                continue
            # if equipment["outagedate"] is not None:
            #     return equipment_outages
            
            if equipment["equipmenttype"]== "ES":
                equipment_type= "Escalator"
            elif equipment["equipmenttype"]=="EL":
                equipment_type= "Elevator"
            equipment_outages.append({
                "type":equipment_type,
                "reason":equipment["reason"],
                "outage_date": equipment["outagedate"],
                "return_serice": equipment["estimatedreturntoservice"],
                "service_area": equipment["serving"]
                
            })
        return equipment_outages
    
    def train_delay(self,station_name, line):
        id = self.long_name_to_id(station_name)
        line_data = self.get_train_line_data(line)
        for line in line_data:
            if line.HasField("trip_update"):
                print(line.trip_update.stop_time_update)
                schedule = line.trip_update.stop_time_update.arrival.time
                arival = line.trip_update.stop_time_update.departure.time
                if arival - schedule > 120:
                    return True
        return False
   
    def station_lines(self, stop_ids):

        train_lines = [
        '1', '2', '3', '4', '5', '6', '7',  # IRT lines
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'M', # IND lines
        'J', 'L', 'N', 'Q', 'R', 'W', 'Z',   # BMT lines
        'S',  # Shuttles
        'SIR' #Staten Island Railway
        ]
        station_trains = []
        for l in train_lines:
            train = self.get_train_line_data(l)
           
            for t in train:
                for update in t.trip_update.stop_time_update:
                   
                    if update.stop_id in stop_ids:
                        
                        if t.trip_update.trip.route_id not in station_trains:
                            station_trains.append(t.trip_update.trip.route_id)
                       

        return station_trains
                        
 
    def station_train_info(self, stop_ids): 
        train_info = []
        train_line = []
        for id in stop_ids:
            t= self.station_lines(stop_ids)
            for i in t:
                if i not in train_line:
                    train_line.append(i)
        print(train_line)

        for t in train_line:
            info = self.get_train_line_data(t)
            
            for i in info:
                if not i.HasField("trip_update"):
                    continue

                for update in i.trip_update.stop_time_update:
                    if update.stop_id in stop_ids:
                        arrival_time = update.arrival.time if update.HasField("arrival") else None
                        current_time = int(time.time())
                        t = max((arrival_time - current_time) // 60, 0)
                        train_info.append({
                            "route": t,
                            "arrival_time": t
                        })
                        break  # Stop after finding one matching stop_id in this trip

                if any(train['route'] == t for train in train_info):
                    break  # Stop checking more trips once we've added info for this line

        return train_info



    
        


       


            



        
