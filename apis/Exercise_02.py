'''

Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint


url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.get(url)
data = response.json()  # returns a dictionary with several objects. every object has certain attributes


# get the emails out of the data dictionary
# use list comprehension instead?!
email_list = []
for user in data['data']:
    user_email = user['email']
    email_list.append(user_email)


pprint(email_list)
