
import re
from urllib import response
import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format, text_format, message
import time
import pandas as pd



from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

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
        self.ipstack = os.environ.get("ipstack")
        self.sessions =requests.Session()

    
    # def get_train_long_name(self, train)->dict:
    #     f = pd.read_csv("backend/src/mta_info/routes.txt")
        
    #     # Filter the dataframe for the specific train
    #     result = f[f["route_short_name"] == train]
        
    #     if not result.empty:
    #         route_id = result.iloc[0]["route_long_name"]
    #         return {train: route_id}
    #     else:
    #         return {}

    # def get_train_trip(self, train)->dict:
    #     f = pd.read_csv("backend/src/mta_info/routes.txt")
        
    #     # Filter the dataframe for the specific train
    #     result = f[f["route_short_name"] == train]
        
    #     if not result.empty:
    #         route_id = result.iloc[0]["route_long_name"]
    #         return {train: route_id}
    #     else:
    #         return {}
           

    # def get_train_stop_id(self, train)->dict:
        
    #     return{}
        

    
    # def get_train(self)->str:
    #     return
    # def get_door(self)->int:
    #     return
    
    # def get_cart(self)->int:
    #     return
    
    # def get_station(self)->str:
    #     return
    
    # def is_train_accessible_at_station(self)->bool:
    #     return
    
    # def elvators_down_at_station(self, station):
    #     return
    # def alternate_accessible_rourtes(self)->list[dict]:
    #     return
    
    # def spefic_line_data(self)->str:
    #     return

    # def is_train_delay(self, train)->bool:
    #     return

    def get_user_coordinate(self):
        ip = requests.get('https://api.ipify.org').text
        location = requests.get(f"http://api.ipstack.com/{ip}?access_key={self.ipstack}").json()
        lat = location["latitude"]
        lon =location["longitude"]
        return lat, lon
                     
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
                if route_id == "R":
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



    # def nearest_station(self):
    #     f = pd.read_csv("backend/src/mta_info/stops.txt")
    #     user_lat, user_lon = self.get_user_coordinate()
    #     stations = []
        
    #     for _, row in f.iterrows():
    #         stop_lat = row["stop_lat"]
    #         stop_lon = row["stop_lon"]
    #         stop_id = row["stop_id"]
    #         distance = haversine(user_lat, user_lon, stop_lat, stop_lon)
            
    #         stations.append({
    #             "stop_id": stop_id,
    #             "stop_name": row["stop_name"],
    #             "distance": distance
    #         })

    #     sorted_data = sorted(stations, key=lambda s: s["distance"])

    #     for station in sorted_data[:-5]:
    #         print(f'{station["stop_name"]} - {station["distance"]:.2f} km')

    #     # return sorted_data[:5]  # top 5 nearest stations


        


    def nearest_station(self):
        f = pd.read_csv("backend/src/mta_info/stops.txt")
        user_lat, user_lon = self.get_user_coordinate()
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
        return sorted_data[:5]  # top 5 nearest stations
