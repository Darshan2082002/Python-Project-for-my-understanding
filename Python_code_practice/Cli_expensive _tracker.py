import json 
from datetime import datetime 
import os
from textwrap import indent

from numpy import save 


Data='expensive.json'

def load_data():
    if not os.path.exists(Data):
        return []
    with open(Data,"r") as file:
        return json.load(file)
def save_expensive(exp):
    with open(Data,"w") as file:
        json.dump(exp,file,indent=4)
def expensive():
    return 