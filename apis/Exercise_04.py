'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": "79",  # insert ID that code knows which user to update
    "first_name": "Monty",
    "last_name": "Python",
    "email": "monty@update.com"
}

put_to_server = requests.put(url, json=body)

response = requests.get(url)

pprint(response.status_code)