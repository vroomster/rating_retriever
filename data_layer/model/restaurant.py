

class Restaurant:

    def __init__(self, yelp_restaurant_name, grubhub_restaurant_name, grubhub_restaurant_id,
        address, city, state, country, phone_number, yelp_rating, yelp_review_count, yelp_url,
        grubhub_url, latitude=None, longitude=None):
        self.yelp_restaurant_name = yelp_restaurant_name
        self.grubhub_restaurant_name = grubhub_restaurant_name
        self.grubhub_restaurant_id = grubhub_restaurant_id
        self.adddress = address
        self.city = city
        self.state = state
        self.country = country
        self.phone_number = phone_number
        self.yelp_rating = yelp_rating
        self.yelp_review_count = yelp_review_count
        self.yelp_url = yelp_url
        self.grubhub_url = grubhub_url
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())
