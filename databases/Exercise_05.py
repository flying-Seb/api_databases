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
# insert all users and all tasks in tables of db --> STILL OPEN (pending)
# check how to fill lookup table user_task --> STILL OPEN
# before inserting: check if data already exists [try/except] --> STILL OPEN

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


def insert_users_db():
    """A function to setup a query and save the users data from the API in tables of the db"""
    # create table object for Users table
    users_table = sqlalchemy.Table('Users', metadata, autoload=True, autoload_with=engine)

    # get JSON data from API
    json_data = get_users()

    # build query and execute by inserting JSON
    query = sqlalchemy.insert(users_table)

    # store every user object in a list which is then passed into the
    result_proxy = connection.execute(query, json_data['data'])
    return


def insert_tasks_db():
    """A function to setup a query and save the tasks data from the API in the tables of the db"""
    # create table object for Tasks table
    tasks_table = sqlalchemy.Table('Tasks', metadata, autoload=True, autoload_with=engine)

    # get JSON data from API
    json_data = get_tasks()

    # build query and execute by inserting JSON
    query = sqlalchemy.insert(tasks_table)
    result_proxy = connection.execute(query, json_data['data'])
    return


def connect_db():
    """setting up the connection to the database"""

    user = os.environ['USER']
    pw = os.environ['PW']

    # try to connect with dev.env file for username and pw
    global engine
    engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{pw}@localhost/API_user_task')
    global connection
    connection = engine.connect()
    global metadata
    metadata = sqlalchemy.MetaData()

    # create table objects for every table in the db
    user_table = sqlalchemy.Table('Users', metadata, autoload=True, autoload_with=engine)
    tasks_table = sqlalchemy.Table('Tasks', metadata, autoload=True, autoload_with=engine)
    return engine, connection, metadata


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


# setting name to main if the program is called directly
if __name__ == '__main__':
    main()
