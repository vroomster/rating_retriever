
class DistanceData:

    def __init__(self, connector):
        self.connector = connector

    '''CREATE TABLE IF NOT EXISTS distances
                 (location_name text not null, grubhub_restaurant_id text not null,
                 distance_from_location real not null)
                 PRIMARY KEY(location_name, grubhub_restaurant_id));'''
    def insert_distances(self, distances=[]):
        query = 'INSERT OR IGNORE INTO distances VALUES (?,?,?)'
        return self.connector.execute_many(query, distances)


    def get_distances(self, location_name):
        query = """SELECT *
                   FROM distances
                   where location_name=? ORDER BY yelp_rating desc, yelp_review_count desc"""
        return self.connector.execute_query(query, (location_name))

"""
    def check_if_restaurant_saved(self, restaurant_id):
        query = 'SELECT COUNT(1) FROM restaurant_data WHERE grubhub_restaurant_id = ?'
        return self.connector.execute_query(query, (restaurant_id,)) == [(1,)]

    def get_reservation_message_history(self, reservation_id):
        last_reservation_message_history_record = self.conn_cursor.execute(
            "select reservation_message_type FROM reservation_messages WHERE reservation_id=? ORDER BY send_date DESC", (reservation_id,)).fetchone()
        last_reservation_message_type = last_reservation_message_history_record[0] if last_reservation_message_history_record else None
        print("Last message in reservation history for reservation {0} is {1}".format(reservation_id, last_reservation_message_type))
        return last_reservation_message_type
"""
