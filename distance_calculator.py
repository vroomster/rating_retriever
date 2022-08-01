from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from time import sleep

from data_layer.location_data import LocationData
from data_layer.distance_data import DistanceData
from data_layer.restaurant_data import RestaurantData

class DistanceCalculator:

    def __init__(self, user_agent, connector):
        self.geolocator = Nominatim(user_agent=user_agent)
        self.location_data = LocationData(connector)
        self.distance_data = DistanceData(connector)
        self.restaurant_data = RestaurantData(connector)

    def get_address_lat_long(self, address, city, state, country):
        location = self.geolocator.geocode(",".join([address, city, state, country]))
        sleep(1)
        return (location.latitude, location.longitude)


    def calculate_distance(self, location1, location2):
        return geodesic(location1, location2).miles

    def calculate_distances_for_all_locations(self):
        return location_data.get_all_locations(location_data)

    def get_distance_to_restaurant(self, location, restaurant):
        if not restaurant.latitude:
            print("Restaurant has no latitude: {}".format(restaurant))
            restaurant.latitude, restaurant.longitude = self.get_address_lat_long(restaurant.adddress,
                restaurant.city, restaurant.state, restaurant.country)
        distance = self.calculate_distance((location.latitude, location.longitude), (restaurant.latitude, restaurant.longitude))
        if distance <= location.max_distance:
            print("Location: {}, restaurant: {}".format(location.name, restaurant.yelp_restaurant_name))
            print("Distance from restaurant to location = {}".format(distance))
            return (location.name, restaurant.grubhub_restaurant_id, distance)

    def get_distances_to_restaurants(self, location, max_distance=None):
        distances_to_location = []
        for restaurant in self.restaurant_data.get_restaurants():
            if max_distance:
                location.max_distance = max_distance
            distance_tuple = self.get_distance_to_restaurant(location, restaurant)
            if distance_tuple:
                distances_to_location.append(distance_tuple)
        print(distances_to_location)
        return distances_to_location

    def add_distances_all_locations(self, max_distance=None):
        for location in self.location_data.get_all_locations():
            print(self.distance_data.insert_distances(self.get_distances_to_restaurants(location, max_distance)))
