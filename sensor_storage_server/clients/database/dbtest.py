from pymongo import MongoClient

from sensor_storage_server.clients.database.database_client import SensorValue, DatabaseClient

if __name__ == "__main__":
    client = DatabaseClient()

    sensor_data = SensorValue(12, "c", "12:00")

    new_id = client.add_value(sensor_data)

    values = client.get_all_values()
    for value in values:
        print(value)
