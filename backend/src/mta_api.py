from nt import environ
from xmlrpc.client import boolean
import requests
import os
from dotenv import load_dotenv


class mta_api():

    def __init__(self):
        load_dotenv()
        self.ACESr= os.environ.get("ACESr")
        self.BDFMSf=os.environ.get("BDFMSf")
        self.G = os.environ.get("G")
        self.JZ = os.environ.get("JZ")
        self.NQRW = os.environ.get("NQRW")
        self.L= os.environ.get("L")
        self.num_1234567S = os.environ("num_1234567S")
        self.SIR = "SIR"


    def get_train(self)->str:
        return
    def get_door(self)->int:
        return
    
    def get_cart(self)->int:
        return
    
    def get_station(self)->str:
        return
    
    def is_train_accessible_at_station(self)->boolean:
        return
    
    def elvators_down_at_station(self, station):
        return
    def alternate_accessible_rourtes(self)->list[dict]:
        return
    
    def spefic_line_data(self)->str:
        return

    def is_train_delay(self, train)->boolean:
        return
    
    


