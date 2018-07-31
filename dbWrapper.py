import sqlite3
from datetime import datetime

path_to_db = "storage.db"
ticks_in_seconds_count = 10 ** 7


class DbWrapper:
    """
    A class for operations with sqlite db
    """

    def __init__(self):
        conn = self.connection
        cur = conn.cursor()

        # drop previous table
        cur.execute("drop table if exists 'results'")

        # create a new table for results
        cur.execute("create table 'results' ('ticks' INTEGER NOT NULL, 'text' TEXT, PRIMARY KEY(`ticks`))")

        conn.commit()
        conn.close()

    @property
    def connection(self):
        return sqlite3.connect(path_to_db)

    @staticmethod
    def convert_date_time_to_ticks(input_date_time):
        t0 = datetime(1, 1, 1)
        seconds = (input_date_time - t0).total_seconds()
        return seconds * ticks_in_seconds_count

    def save(self, date_time, text):
        conn = self.connection
        cur = conn.cursor()

        ticks = DbWrapper.convert_date_time_to_ticks(date_time)
        params = (ticks, text)
        cur.execute("insert into 'results' (ticks, text) values (?,?)", params)

        conn.commit()
        conn.close()

    def load_last_record(self):
        conn = self.connection
        cur = conn.cursor()

        cur.execute("select text from 'results' order by ticks desc limit 1")
        raw_text = cur.fetchone()
        # fix string format
        result = None if not raw_text else raw_text[0].replace(r"\n", "\n")

        conn.close()

        return result
