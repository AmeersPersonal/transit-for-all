from urllib import response
import requests
import os
from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
from google.protobuf import json_format, text_format, message
import time
import pandas

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

  
    def response_handler(self, line):
        url = self.feeds.get(lines)
        feed = gtfs_realtime_pb2.FeedMessage()
        response = self.sessions.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed to fetch feed: {response.status_code} - {response.text}")
        
        feed.ParseFromString(response.content)
        feed_json = json_format.MessageToJson(feed)
        

    
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

