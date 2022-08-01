import sqlite3
from .connector import Connector


class SqliteConnector(Connector):

    def __init__(self, source_name):
        self.source_name = source_name
        self.conn = sqlite3.connect(source_name)
        self.conn_cursor = self.conn.cursor()

    def execute_query(self, query, values):
        if values:
            value = self.conn_cursor.execute(query, values).fetchall()
        else:
            value = self.conn_cursor.execute(query).fetchall()
        self.conn.commit()
        return value

    def execute_many(self,query, many_values):
        value = self.conn_cursor.executemany(query, many_values)
        self.conn.commit()
        return value
