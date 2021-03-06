from datetime import date, datetime
from enum import Enum
from uuid import uuid4
import json

class Status(Enum):
    CLOSED = 0
    OPEN = 1
    ANGLED = 2
    ERROR = -1

class Window():
    def __init__(self, ID, room, name):
        self.ID = str(ID)
        self.room = room
        self.name = str(name)
        self.timestamp = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        self.status = Status.CLOSED.value

        print(self.timestamp)

    def updateTimestamp(self):
        self.timestamp = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))

    def checkTimestamp(self):
        """ return true if timestamp is valid -> not older than 10 seconds ago """
        currentTime = datetime.now()
        difference = currentTime - datetime.strptime(self.timestamp.strftime, "%y-%m-%d %H:%M:%S")

        return (difference.total_seconds() < 10)
    
    def getDict(self):
        d = {
            "_id": self.ID,
            "room": self.room.getDict(),
            "name": self.name,
            "timestamp": self.timestamp,
            "status": self.status
        }
        return d
    
    def getJson(self):
        return json.dumps(self.getDict(self), indent="  ")

class Room():
    def __init__(self, name, ID = str(uuid4())):
        self.ID = str(ID)
        self.name = name

    def getDict(self):
        d = {
            "_id": self.ID,
            "name": self.name
        }
        return d
    
    def getJson(self):
        return json.dumps(self.getDict(self), indent="  ")
