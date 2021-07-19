from time import sleep
from difflib import SequenceMatcher
from collections import Counter
from api_client.grubhub_api_client import GrubhubApiClient
from api_client.yelp_api_client import YelpApiClient

from data_layer.restaurant_data import RestaurantData


class RatingRetriever():
    def __init__(self, connector):
        self.yelp_api_client = YelpApiClient()
        self.restaurant_data = RestaurantData(connector)


    def get_best_match(self, yelp_businesses, grubhub_restaurant):
        #print(yelp_businesses)
        best_match = max(yelp_businesses, key=lambda x: self.get_similarity_score(x.name.lower(), grubhub_restaurant.name.lower()))
        return best_match if self.get_similarity_score(best_match.name.lower(), grubhub_restaurant.name.lower()) > 0.8 else None


    def get_similarity_score(self, name1, name2):
        if name1 == name2:
            return 1.0
        elif name1 in name2 or name2 in name1:
            return 0.95
        else:
            return SequenceMatcher(None, name1, name2).ratio()

#    def common_words_score(self, name1, name2):

        #def check_page_tracker():
        #print(yelp_api_client.search_matches(name=restaurant.name, address1=address.street_address,
        #    city=address.address_locality, state=address.address_region, country=address.address_country))
    def retrieve_restaurants(self, api_key, longitude, latitude, page_number):
        counter = 0
        while True:
            matched_restaurants = []
            search_results = GrubhubApiClient(api_key).get_restaurants(
                longitude=longitude, latitude=latitude, page_size=100, page_number=page_number)
            print("Search Result Stats: {}".format(search_results.stats))
            print("Page Tracker: {}".format(search_results.pager))
            for grubhub_restaurant in search_results.results:
                counter+=1
                address=grubhub_restaurant.address
                #print("Checking restaurant {} with id {}".format(grubhub_restaurant.name, grubhub_restaurant.restaurant_id))
                if self.restaurant_data.check_if_restaurant_saved(grubhub_restaurant.restaurant_id):
                    #print("Restaurant has already been saved! Skipping. GH {}".format(grubhub_restaurant.name))
                    continue
                phone_number = "+{}{}".format(grubhub_restaurant.phone_number.country_code, grubhub_restaurant.phone_number.phone_number)
                yelp_businesses_matches = self.yelp_api_client.search_by_phone(phone_number)
                if not yelp_businesses_matches or not yelp_businesses_matches.businesses or len(yelp_businesses_matches.businesses) < 1:
                    #print("Error! No Yelp businesses inside of matches: GH: {}".format(grubhub_restaurant.name))
                    yelp_businesses_matches = self.yelp_api_client.search_matches(grubhub_restaurant.name, address.street_address,
                        address.address_locality, address.address_region, address.address_country) or []
                    #print("Searched with Yelp matches api -- {}".format(yelp_businesses_matches.businesses))
                if yelp_businesses_matches and yelp_businesses_matches.businesses and len(yelp_businesses_matches.businesses) >= 1:
                    best_business_match = self.get_best_match(yelp_businesses_matches.businesses, grubhub_restaurant)
                    if not best_business_match:
                        print("No similar name match Found! {}".format(grubhub_restaurant.name))
                        continue
                        ##TODO: Here, the code needs to add these restaurants to a list that can be processed at the end of pulling all the restaurants
                        for index, business in enumerate(yelp_businesses_matches.businesses):
                            print(">>>>>>>> {}: {}".format(index, business))
                        choice = -1
                        try:
                            choice = int(input("Enter index of restaurant match starting at 0, anything else to skip: "))
                        except ValueError as ve:
                            print("Skipping restaurant match")
                        if choice >= 0 and choice <= len(yelp_businesses_matches.businesses):
                            best_business_match = yelp_businesses_matches.businesses[choice]
                    else: #found business match
                        print("Found match GH: {} ---- Yelp: {}".format(grubhub_restaurant.name, best_business_match.name))
                        grubhub_url = "https://www.grubhub.com/restaurant/{}/{}".format(grubhub_restaurant.merchant_url_path, grubhub_restaurant.restaurant_id)
                        yelp_url = ""
                        if best_business_match.url:
                            yelp_url = best_business_match.url.split('?')[0]
                        match = (best_business_match.name, grubhub_restaurant.name, grubhub_restaurant.restaurant_id,
                            address.street_address, address.address_locality, address.address_region, best_business_match.location.country,
                            phone_number, best_business_match.rating, best_business_match.review_count, yelp_url, grubhub_url,
                            best_business_match.coordinates.latitude, best_business_match.coordinates.longitude)
                        matched_restaurants.append(match)
                else:
                    print("Still no matches after matches api! -- {}".format(grubhub_restaurant.name))
                sleep(1)

            print("Found {} matched restaurants".format(len(matched_restaurants)))
            print("Inserted restaurants: {}".format(self.restaurant_data.insert_restaurants(matched_restaurants)))

            ##TODO: check number of inserted restaurants in the table

            if search_results.pager.current_page == search_results.pager.total_pages or page_number == search_results.pager.total_pages:
                break
            elif search_results.pager.current_page > search_results.pager.total_pages or page_number > search_results.pager.total_pages:
                print("ERROR! We exceeded the page check somehow!")
                break
            page_number += 1
            print("New page number ==== {}".format(page_number))



'''
    def check_match(self, grubhub_restaurant, yelp_restaurant):
        lowercase_yelp_restaurant_name = yelp_restaurant.name.lower()
        lowercase_gh_restaurant_name = grubhub_restaurant.name.lower()
        if lowercase_yelp_restaurant_name in lowercase_gh_restaurant_name or lowercase_gh_restaurant_name in lowercase_yelp_restaurant_name:
            return True
        elif self.similar(lowercase_yelp_restaurant_name, lowercase_gh_restaurant_name) > 0.8:
            return True
        else:
            #print("Restaurant name doesn't match Yelp: {} --- GH: {}".format(yelp_restaurant.name, grubhub_restaurant.name))
            return False
        #elif yelp_restaurant.location.address1 != grubhub_restaurant.address.street_address:
            #print("Restaurant address doesn't match Yelp: {} --- GH: {}".format(yelp_restaurant.location.address1, grubhub_restaurant.address.street_address))
            #return False
        #return True
'''







#print(restaurant_data.check_if_restaurant_saved('Burma Superstar'))


#yelp_api_client.search_by_business_id("WavvLdfdP6g8aZTtbBQHTw")
