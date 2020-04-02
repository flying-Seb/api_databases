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
# requests.get all users and all tasks from API --> done

import requests
from pprint import pprint
import json

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"


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


all_users = get_users()
all_tasks = get_tasks()

pprint(all_users)
print("/n")
print("---------------------------------------------")
print("/n")
pprint(all_tasks)

# setting name to main if the program is called directly
# if __name__ == '__main__':
#    main()