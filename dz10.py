import sqlite3
from datetime import datetime

current_datetime = datetime.now()
a = 10

connection = sqlite3.connect("weather_cher.sl3", 5)
cur = connection.cursor()
cur.execute("DECLARE @current_datetime INT;")
connection.commit()

connection.close()