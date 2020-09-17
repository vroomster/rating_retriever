from rating_retriever import RatingRetriever
from distance_calculator import DistanceCalculator

from data_layer.db.sqlite3_connector import SqliteConnector


connector = SqliteConnector('local_sqlite.db')
api_key = "7ff0afec-cf27-4893-b0bf-a85d1f681d72"
tracy = (-121.42600251, 37.73958206)
emma = (-122.437310, 37.770671)
dublin_pleasanton = (-121.876827, 37.693570)
oakland = (-122.255002, 37.814228)
locations = [dublin_pleasanton, oakland, tracy, emma]

#for location in locations:
#    RatingRetriever(connector).retrieve_restaurants(api_key=api_key,longitude=location[0], latitude=location[1], page_number=1)

DistanceCalculator("vroomSoft", connector).add_distances_all_locations()
