'''

Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(base_url + "/121")
response1 = requests.delete(base_url + "/120")

print(response.status_code)
print(response1.status_code)

response_confirm = requests.get(base_url)
data = response_confirm.json()
pprint(data)
