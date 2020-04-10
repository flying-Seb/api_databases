'''

Using the API from the API section, write a program that makes a request to
get all of the users and all of their tasks.

Create tables in a new local database to model this data.

Think about what tables are required to model this data. Do you need two tables? Three?

Persist the data returned from the API to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

# first: paper and pen for architecture! --> done
# database created over the CLI --> done
# create connection to db. setup login credentials for mysql in a separate file as environment variables --> done
# requests.get all users and all tasks from API --> done
# insert all users and all tasks in tables of db --> done
# check how to fill lookup table user_task --> done
# before inserting: check if data already exists (update on duplicate) --> done

import requests
import pymysql
import sqlalchemy
from pprint import pprint
import json
import os

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"


def main():
    connect_db()
    insert_users_db()
    insert_tasks_db()
    update_lookup()


def insert_users_db():
    """A function to setup a query and save the users data from the API in tables of the db"""

    # get JSON data from API
    json_data = get_users()

    # call the insert_try_exc function and pass the table and json_data is arguments
    insert_try_exc(users_table, json_data)
    return


def insert_tasks_db():
    """A function to setup a query and save the tasks data from the API in the tables of the db"""

    # get JSON data from API
    json_data = get_tasks()

    # call the insert_try_exc function and pass the table and json_data is arguments
    insert_try_exc(tasks_table, json_data)
    return


def update_lookup():
    """Update the lookup table user_task in the db with the new data every time the program runs"""
    from sqlalchemy.dialects.mysql import insert
    from sqlalchemy.sql import alias, select

    # create a join on both task_id and user_id
    join_stmt = tasks_table.join(users_table, users_table.columns.id == tasks_table.columns.userId)
    func_query = sqlalchemy.select([tasks_table.columns.id, users_table.columns.id]).select_from(join_stmt)
    try:
        connection.execute(func_query)
    except:
        query = sqlalchemy.delete(lookup_table)
        connection.execute(query)
        connection.execute(func_query)
    return


def connect_db():
    """Setting up the connection to the database"""

    user = os.environ['USER']
    pw = os.environ['PW']

    # try to connect with dev.env file for username and pw
    global engine
    engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{pw}@localhost/API_user_task')
    global connection
    connection = engine.connect()
    global metadata
    metadata = sqlalchemy.MetaData()

    # create all tables as global variables
    global users_table
    users_table = sqlalchemy.Table('Users', metadata, autoload=True, autoload_with=engine)
    global tasks_table
    tasks_table = sqlalchemy.Table('Tasks', metadata, autoload=True, autoload_with=engine)
    global lookup_table
    lookup_table = sqlalchemy.Table('user_task', metadata, autoload=True, autoload_with=engine)
    return engine, connection, metadata, users_table, tasks_table, lookup_table


def get_users():
    """A function to get all users and save it in a JSON format"""

    response = requests.get(users_url)
    all_users = response.json()
    return all_users


def get_tasks():
    """A function to get all tasks and save it in a JSON format"""

    response = requests.get(tasks_url)
    all_tasks = response.json()
    return all_tasks


def insert_try_exc(table, json_data):
    """Inserts data in a specific table passed as an argument"""

    try:
        ins = sqlalchemy.insert(table)
        connection.execute(ins, json_data['data'])
    except:
        if table == users_table or table == tasks_table:
            query = sqlalchemy.delete(table).where(table.columns.id != "")
            connection.execute(query)
            query1 = sqlalchemy.insert(table)
            connection.execute(query1, json_data['data'])
        else:
            query2 = sqlalchemy.delete(table).where(table.columns.userId != "")
            connection.execute(query2)
            query3 = sqlalchemy.insert(table)
            connection.execute(query3, json_data['data'])
    return


# setting name to main if the program is called directly
if __name__ == '__main__':
    main()
