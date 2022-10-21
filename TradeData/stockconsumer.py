import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer
import datetime
from .models import getCurrentValueOfStock 

class stockConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            self.send(json.dumps({"niftyValue": getCurrentValueOfStock()}))
            sleep(1)

