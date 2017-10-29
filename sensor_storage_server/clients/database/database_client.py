from pymongo import MongoClient

class SensorValue:
    def __init__(self, value, unit, time):
        self.value = value
        self.unit = unit
        self.time = time

class DatabaseClient:

    def __init__(self, host="localhost", port=27017):
        self.client = MongoClient(host, port)
        self.database = self.client["test"]
        self.collection = self.database.sensor_values

    def add_value(self, sensor_value):
        return self.collection.insert_one(sensor_value.__dict__)

    def get_all_values(self):
        return self.collection.find()
