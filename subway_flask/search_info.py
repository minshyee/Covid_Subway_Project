from pymongo import MongoClient
from subway_flask.db_info import MONGO_URI, DATABASE_NAME



def transfer_type(rain, holiday):
    if rain ==  None:
        rain = 0
    else:
        rain = 1

    if holiday ==  None:
        holiday = 0
    else:
        holiday = 1
    return rain, holiday


def find_bus(station, line):
    client =MongoClient(MONGO_URI)
    database = client[DATABASE_NAME]
    collection = database['subway']
    data = collection.find( { "s_name" : station, "line": line })
    st_code = data[0]['st_num']
    collection_bus = database['bus']
    try:
        data_bus = collection_bus.find({"st_code":st_code})
        bus_cnt = data_bus[0]['bus_cnt']
    except:
        bus_cnt = 0
    return bus_cnt
