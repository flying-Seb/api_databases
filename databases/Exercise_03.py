'''
Update all films in the film table to a rental_duration value of 10,
if the length of the movie is more than 150.

'''


import sqlalchemy
import pymysql

engine = sqlalchemy.create_engine('mysql+pymysql://root:123__UmWeLT??GO!@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.update(film).values(rental_duration=10).where(film.columns.length > 150)
result_proxy = connection.execute(query)




