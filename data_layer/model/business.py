

class Restaurant:

    def __init__(self, name, address, city, state, country, phone_number,
            delivery_service_details = {}, rating_details = {},  latitude=None, longitude=None):
        self.name = name
        self.adddress = address
        self.city = city
        self.state = state
        self.country = country
        self.phone_number = phone_number
        self.latitude = latitude
        self.longitude = longitude
        self.ratings = ratings
        self.delivery_services = delivery_services

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())
