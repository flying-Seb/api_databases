'''

Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

1) Select all the actors with the first name of your choice
2) Select all the actors and the films they have been in
3) Select all the actors that have appeared in a category of your choice
4) Select all the comedic films and sort them by rental rate
5) Using one of the statements above, add a GROUP BY statement of your choice
6) Using one of the statements above, add a ORDER BY statement of your choice

'''

import sqlalchemy
import pymysql
from pprint import pprint

# setup engine and connection for all tasks

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

''' 1) select all actors with first name "PENELOPE" '''
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)
actor_query = sqlalchemy.select([actor]).where(actor.columns.first_name == 'PENELOPE')
result_proxy = connection.execute(actor_query)
result_set = result_proxy.fetchmany(5)
print('Exercise 1)')
pprint(result_set)

''' 2) select all actors and the films they have been in '''

# the actor object can be used from above
film_actor = sqlalchemy.Table('film_actor', metadata, autoload=True, autoload_with=engine)
film = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

# setting up the join statement
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).\
                 join(film, film.columns.film_id == film_actor.columns.film_id)

# select statement of the join statement
query = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.first_name, actor.columns.last_name]).\
        select_from(join_statement)

# execute the query and fetch it
result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(15)
print('Exercise 2)')
pprint(result_set)


''' 3) select all actors that have appeared in the comedy category '''

# use another join statement




