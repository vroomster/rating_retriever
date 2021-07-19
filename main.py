from rating_retriever import RatingRetriever
from distance_calculator import DistanceCalculator

from data_layer.db.sqlite3_connector import SqliteConnector


connector = SqliteConnector('local_sqlite.db')
api_key = "c06b9d3e-50cd-40d7-ab34-6cca4b753d1c"
tracy = (-121.42600251, 37.73958206)
dublin_pleasanton = (-121.876827, 37.693570)
oakland = (-122.255002, 37.814228)
kira = (-122.423792, 37.744099)
ballard = (-122.373690, 47.673256)
leschi_airbnb = (-122.292964, 47.592030)
queen_anne_airbnb = (-122.35331587688077, 47.619732850857964)
nams = (-122.17014675065933, 47.61857088557854)
fadh = (-118.4547766, 33.9766901)

locations = [fadh]

for location in locations:
    RatingRetriever(connector).retrieve_restaurants(api_key=api_key,longitude=location[0], latitude=location[1], page_number=1)

DistanceCalculator("vroomSoft", connector).add_distances_all_locations()
