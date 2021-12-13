from pymongo import MongoClient
import os
import csv

# MongoDB authorization
HOST = 'cluster0.0xhgi.mongodb.net'
USER = 'minshyee'
PASSWORD = 'smh0115mh'
DATABASE_NAME = 's3project'
COLLECTION_NAME = 'bus'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

# 버스 정류장 데이터 저장
CSV_FILENAME = 'bus_stop_cnt.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)

with open(CSV_FILEPATH, 'r',encoding='UTF8') as csv_file:
    data = csv.DictReader(csv_file)

    client =MongoClient(MONGO_URI)
    database = client[DATABASE_NAME]
    collection = database[COLLECTION_NAME]
    collection.insert_many(data)




