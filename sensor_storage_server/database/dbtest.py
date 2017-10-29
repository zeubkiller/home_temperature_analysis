from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('localhost', 27017)

    db = client.test_database
    print(db)

    collection = db.test_collection
    print(collection)

    sensor_data = {"sensor_type":"temperature",
                   "value":12,
                   "unit":"c"}

    sensor_data_list = db.sensor_data
    new_sensor_data_id = sensor_data_list.insert_one(sensor_data).inserted_id
    print(new_sensor_data_id)

    print(db.collection_names(include_system_collections=False))
