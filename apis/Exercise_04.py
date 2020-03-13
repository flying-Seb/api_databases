'''

Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    'id': 119,  # server has to know which user to update
    'first_name': 'jane',
    'last_name': 'doe',
    'email': 'jane@doe.com'
}

# using a put request to update user data
response = requests.put(base_url, json=body)

print(f"Status code after PUT: {response.status_code}")

response = requests.get(base_url)
pprint(response.json())

