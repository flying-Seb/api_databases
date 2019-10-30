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
from sqlalchemy import func

engine = sqlalchemy.create_engine('mysql+pymysql://root:123__UmWeLT??GO!@localhost/sakila')
connection = engine.connect()
meta_data = sqlalchemy.MetaData()

# creating objects for the queries
actor = sqlalchemy.Table('actor', meta_data, autoload=True, autoload_with=engine)  # creates a table object
film = sqlalchemy.Table('film', meta_data, autoload=True, autoload_with=engine)
film_actor = sqlalchemy.Table('film_actor', meta_data, autoload=True, autoload_with=engine)
category = sqlalchemy.Table('category', meta_data, autoload=True, autoload_with=engine)
film_category = sqlalchemy.Table('film_category', meta_data, autoload=True, autoload_with=engine)
newTable = sqlalchemy.Table('newTable', meta_data, autoload=True, autoload_with=engine)


# 1) all actors with a specific first name
print("# 1) all actors with a specific first name")
query = sqlalchemy.select([actor]).where(actor.columns.first_name == "PENELOPE")
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()  # fetchall() can be used to select all the elements
pprint(result_set)
print("--------------")

# 2) all actors and films they have been in
print("# 2) all actors and films they have been in")
join_actor_film_actor = actor.join(film_actor, film_actor.columns.actor_id == actor.columns.actor_id)
join_statement = join_actor_film_actor.join(film, film.columns.film_id == film_actor.columns.film_id)

film_actor_query = sqlalchemy.select([film.columns.film_id, film.columns.title, actor.columns.actor_id, actor.columns.first_name, actor.columns.last_name]).select_from(join_statement)

result_proxy_fa = connection.execute(film_actor_query)
result_set_fa = result_proxy_fa.fetchmany(25)
pprint(result_set_fa)
print("--------------")

# 3) all the actors of one category
print("# 3) all the actors of one category")
join_category_film_category = category.join(film_category, film_category.columns.category_id == category.columns.category_id)
join_film_category_film_actor = join_category_film_category.join(film_actor, film_actor.columns.film_id == film_category.columns.film_id)
join_film_actor_actor = join_film_category_film_actor.join(actor, actor.columns.actor_id == film_actor.columns.actor_id)

actor_category_query = sqlalchemy.select([actor.columns.actor_id, actor.columns.first_name, category.columns.name]).select_from(join_film_actor_actor).where(category.columns.category_id == '15')
result_proxy_ac = connection.execute(actor_category_query)
result_set_ac = result_proxy_ac.fetchmany(25)
pprint(result_set_ac)

print("--------------")

# 4) all comedy films by rental rate
print("# 4) all comedy films by rental rate")
join_category_film_category = category.join(film_category, film_category.columns.category_id == category.columns.category_id)
join_fc_film = join_category_film_category.join(film, film.columns.film_id == film_category.columns.film_id)
category_comedy_query = sqlalchemy.select([film.columns.film_id, film.columns.title]).select_from(join_fc_film).where(category.columns.name == 'Comedy').order_by(sqlalchemy.desc(film.columns.replacement_cost))

result_proxy_comedy = connection.execute(category_comedy_query)
result_set_comedy = result_proxy_comedy.fetchmany(10)
pprint(result_set_comedy)


print("--------------")

# 5) example with group_by
print("# 5) example with group_by")

query_group = film.with_entities(film.columns.title, func.sum(film.columns.rental_rate)).group_by(film.columns.rental_rate)
result_proxy_group = connection.execute(query_group)
result_set_group = result_proxy_group.fetchall()
pprint(result_set_group)
# ?????????????


