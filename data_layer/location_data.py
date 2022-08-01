from .model.location import Location

class LocationData:

    def __init__(self, connector):
        self.connector = connector

    '''CREATE TABLE IF NOT EXISTS locations
                 (location_name text not null, address text not null,
                 city text not null, state text not null, country text not null,
                 latitude real not null, longitude real not null)
                 PRIMARY KEY(location_name));'''
    def insert_locations(self, locations=[]):
        query = 'INSERT OR IGNORE INTO locations VALUES (?,?,?,?,?,?,?)'
        return self.connector.execute_many(query, restaurants)

    def get_all_locations(self):
        query = """SELECT *
                   FROM locations"""
        return [Location(*location_tuple) for location_tuple in self.connector.execute_query(query, None)]

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
