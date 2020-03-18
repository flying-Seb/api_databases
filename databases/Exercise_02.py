'''

Consider each of the tasks below as a separate database query. Using SQLAlchemy, which is the necessary code to:

1) Select all the actors with the first name of your choice
2) Select all the actors and the films they have been in
3) Select all the actors that have appeared in a category of your choice
4) Select all the comedy films and sort them by rental rate
5) Using one of the statements above, add a GROUP BY statement of your choice
6) Using one of the statements above, add a ORDER BY statement of your choice

'''

from sqlalchemy import desc
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

# the actor and the film_actor object can be used from above for this query
category = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
film_cat = sqlalchemy.Table('film_category', metadata, autoload=True, autoload_with=engine)

# create new join statement for this query
join_statement = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id).\
                 join(film_cat, film_cat.columns.film_id == film_actor.columns.film_id).join(\
                 category, category.columns.category_id == film_cat.columns.category_id)

# select statement of the join statement
query = sqlalchemy.select([category.columns.name, actor.columns.first_name,\
                           actor.columns.last_name]).where(category.columns.name == 'Comedy')\
                           .select_from(join_statement)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchmany(25)
print('Exercise 3)')
pprint(result_set)


''' 4) select all comedy films and sort by rental rate '''

# use category, film and film_cat from previous exercises
# create join from category over film_cat to film to access rental_rate
join_statement = category.join(film_cat, film_cat.columns.category_id == category.columns.category_id).\
                 join(film, film.columns.film_id == film_cat.columns.film_id)

query = sqlalchemy.select([category.columns.name, film.columns.title, film.columns.rental_rate]).where(category.columns.\
        name == 'Comedy').order_by(desc(film.columns.rental_rate)).select_from(join_statement)

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print('Exercise 4)')
pprint(result_set)
