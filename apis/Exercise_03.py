'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'example@example.org'
}

response = requests.post(base_url, json=body)

# change the response to see the new data
response = requests.get(base_url)
data = response.json()

pprint(data)
