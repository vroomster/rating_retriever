from .model.restaurant import Restaurant

class RestaurantData:

    def __init__(self, connector):
        self.connector = connector

    '''CREATE TABLE IF NOT EXISTS restaurant_data
                 (yelp_restaurant_name text not null, grubhub_restaurant_name text not null,
                 grubhub_restaurant_id text not null,
                 adddress text not null, city text not null,
                 state text not null, country text not null, phone_number text not null,
                 yelp_rating text not null, yelp_review_count integer not null, yelp_url text not null,
                 grubhub_url text not null, latitude real not null, longitude real not null,
                 PRIMARY KEY(grubhub_restaurant_name, phone_number));'''
    def insert_restaurants(self, restaurants=[]):
        query = 'INSERT OR IGNORE INTO restaurant_data VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
        return self.connector.execute_many(query, restaurants)

    def get_restaurants_sorted_by_rating(self, city, min_rating=3.5):
        query = """SELECT *
                   FROM restaurant_data
                   where city=? AND yelp_rating>?
                   ORDER BY yelp_rating desc, yelp_review_count desc"""
        return [Restaurant(*tuple) for tuple in self.connector.execute_query(query, (city,min_rating,))]

    def get_restaurants(self, min_rating=3.5):
        query = """SELECT *
                   FROM restaurant_data
                   where yelp_rating>?"""
        restaurants = self.connector.execute_query(query, (min_rating,))
        return [Restaurant(*tuple) for tuple in restaurants]

#The Sycamore|The Sycamore|420117|2140 Mission St|San Francisco|CA|US|+14152527704|4.0|728|https://www.yelp.com/biz/the-sycamore-san-francisco?adjust_creative=yQI_C5jXcgovEPWtApC-GA&utm_campaign=yelp_api_v3&utm_medium=api_v3_phone_search&utm_source=yQI_C5jXcgovEPWtApC-GA|https://www.grubhub.com/restaurant/the-sycamore-2140-mission-st-san-francisco/420117
    def check_if_restaurant_saved(self, restaurant_id):
        query = 'SELECT COUNT(1) FROM restaurant_data WHERE grubhub_restaurant_id = ?'
        return self.connector.execute_query(query, (restaurant_id,)) == [(1,)]

"""
    def get_reservation_message_history(self, reservation_id):
        last_reservation_message_history_record = self.conn_cursor.execute(
            "select reservation_message_type FROM reservation_messages WHERE reservation_id=? ORDER BY send_date DESC", (reservation_id,)).fetchone()
        last_reservation_message_type = last_reservation_message_history_record[0] if last_reservation_message_history_record else None
        print("Last message in reservation history for reservation {0} is {1}".format(reservation_id, last_reservation_message_type))
        return last_reservation_message_type
"""
