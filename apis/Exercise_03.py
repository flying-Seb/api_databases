'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''





















'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Sherlock",
    "last_name": "Holmes",
    "email": "sherlock@holmes.com"
}

post_to_server = requests.post(url, json=body)

response = requests.get(url)

pprint(response.content)
'''