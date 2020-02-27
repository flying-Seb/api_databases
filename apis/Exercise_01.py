'''
Using the requests package, make a GET request to the api behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users

Print out:

    - the status code
    - the encoding of the response
    - the text of the response body

'''




























'''
# ask Johnny about setting up a venv for every new project in the same folder?
# activate every time before starting to work??

import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

server_response = requests.get(url)

# print(server_response.status_code)
# print(server_response.encoding)
pprint(server_response.content)
'''