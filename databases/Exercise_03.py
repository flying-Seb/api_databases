'''

Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''

import sqlalchemy
import pymysql


eng = sqlalchemy.create_engine('mysql+pymysql://user:password@localhost/sakila')
con = eng.connect()
metadata = sqlalchemy.MetaData()

film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=eng)

query = sqlalchemy.update(film).values(rental_duration=15).where(film.columns.length > 180)

result = con.execute(query)
