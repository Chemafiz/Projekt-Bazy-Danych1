import psycopg2
from inserty import *


# Connect to the database
conn = psycopg2.connect("postgres://ljawypfv:1fhvD5FHUkoKLkHkgm24i5BUEpIu3cVg@rogue.db.elephantsql.com/ljawypfv")

cur = conn.cursor()
print(wyswietl_przystanki(3, cur))

cur.close()
conn.close()





