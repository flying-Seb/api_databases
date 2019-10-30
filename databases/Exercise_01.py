'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''


import sqlalchemy
import pymysql


engine = sqlalchemy.create_engine('mysql+pymysql://root:123__UmWeLT??GO!@localhost/sakila')
connection = engine.connect()
meta_data = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', meta_data, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', meta_data, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', meta_data, autoload=True, autoload_with=engine)

print(actor.columns.keys())
print(film.columns.keys())
print(category.columns.keys())


