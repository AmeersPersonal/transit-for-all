
import re
from urllib import response
import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format, text_format, message
import time
import pandas as pd

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

    
    def get_train_long_name(self, train)->dict:
        f = pd.read_csv("backend/src/mta_info/routes.txt")
        
        # Filter the dataframe for the specific train
        result = f[f["route_short_name"] == train]
        
        if not result.empty:
            route_id = result.iloc[0]["route_long_name"]
            return {train: route_id}
        else:
            return {}

    def get_train_trip(self, train)->dict:
        f = pd.read_csv("backend/src/mta_info/routes.txt")
        
        # Filter the dataframe for the specific train
        result = f[f["route_short_name"] == train]
        
        if not result.empty:
            route_id = result.iloc[0]["route_long_name"]
            return {train: route_id}
        else:
            return {}
           

    def get_train_stop_id(self, train)->dict:
        
        return{}
        

    
    def get_train(self)->str:
        return
    def get_door(self)->int:
        return
    
    def get_cart(self)->int:
        return
    
    def get_station(self)->str:
        return
    
    def is_train_accessible_at_station(self)->bool:
        return
    
    def elvators_down_at_station(self, station):
        return
    def alternate_accessible_rourtes(self)->list[dict]:
        return
    
    def spefic_line_data(self)->str:
        return

    def is_train_delay(self, train)->bool:
        return

    def stop_id_to_long_name(self, stop_id):
        f= pd.read_csv("backend/src/mta_info/stops.txt")
        result = f[f["stop_id"] == stop_id]
        
        if not result.empty:
            stop_name = result.iloc[0]["stop_name"]
            return stop_name
        else:
            return 
        


    def test(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        response = self.sessions.get(self.feeds.get("NQRW"))

        if response.status_code != 200:
            raise Exception(f"Failed to get GTFS data: {response.status_code} - {response.text}")

        feed.ParseFromString(response.content)
        for entity in feed.entity:
            if entity.HasField("trip_update"):
                route_id= entity.trip_update.trip.route_id
                if route_id == "R":
                    continue
        return feed


       
    


    # Load GTFS files
    

    def get_train_stops(self, train_short_name="N"):
        routes = pd.read_csv("backend/src/mta_info/routes.txt")
        trips = pd.read_csv("backend/src/mta_info/trips.txt")
        stop_times = pd.read_csv("backend/src/mta_info/stop_times.txt")
        stops = pd.read_csv("backend/src/mta_info/stops.txt")
        # 1. Get route_id for the N train
        route_ids = routes[routes["route_short_name"] == train_short_name]["route_id"]
        print(route_ids)
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

    # 🔍 Example usage:




