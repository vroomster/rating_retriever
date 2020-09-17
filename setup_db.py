import sqlite3

source_name = 'local_sqlite.db'
conn = sqlite3.connect(source_name)
conn_cursor = conn.cursor()


# Create table
conn_cursor.execute('''CREATE TABLE IF NOT EXISTS restaurant_data
                 (yelp_restaurant_name text not null, grubhub_restaurant_name text not null,
                 grubhub_restaurant_id text not null,
                 adddress text not null, city text not null,
                 state text not null, country text not null, phone_number text not null,
                 yelp_rating text not null, yelp_review_count integer not null, yelp_url text not null,
                 grubhub_url text not null, latitude real not null, longitude real not null,
                 PRIMARY KEY(grubhub_restaurant_id));''')



conn_cursor.execute('''CREATE TABLE IF NOT EXISTS locations
                 (name text not null, address text not null,
                 city text not null, state text not null, country text not null,
                 latitude real not null, longitude real not null,
                 PRIMARY KEY(name));''')


conn_cursor.execute('''CREATE TABLE IF NOT EXISTS distances
                 (location_name text not null, grubhub_restaurant_id text not null,
                 distance_from_location real not null, max_distance real,
                 PRIMARY KEY(location_name, grubhub_restaurant_id));''')


# Insert a row of data

# Insert a row of data
# conn_cursor.execute("INSERT OR IGNORE INTO reservation_messages VALUES ('HMCTCRWMZM', '2018-12-25','BOOKING')")

locations = [('Amma and Abba', '548 Liz Terrace', 'Tracy', 'CA', 'USA', 37.759690, -121.535225),
             ('Niha', '271 Amber Drive', 'San Francisco', 'CA', 'USA', 37.744570, -122.443170),
             ('Emma', '840 Waller St', 'San Francisco', 'CA', 'USA', 37.770629, -122.436870)]
conn_cursor.executemany('INSERT OR IGNORE INTO locations VALUES (?,?,?,?,?,?,?)', locations)

# Save (commit) the changes
conn.commit()

#for row in conn_cursor.execute("SELECT * from reservation_messages"):
#    print(row)


# Create table
#conn_cursor.execute('''CREATE TABLE IF NOT EXISTS competitive_history
#             (client_id text not null, listing_id text not null, report_date text not null, check_in text not null,
#             check_out text not null, listing_rank integer, price text, all_prices text not null,
#             price_rank integer,
#             PRIMARY KEY(client_id,listing_id,report_date,check_in,check_out));''')




# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# conn_cursor.execute("SELECT * from reservation_messages WHERE send_date = "
#                        "(select MAX(send_date) FROM reservation_messages WHERE reservation_id=?)", (reservation_id,))
