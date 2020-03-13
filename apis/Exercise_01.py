'''
Using the requests package, make a GET request to the API behind this endpoint:

    http://demo.codingnomads.co:8080/tasks_api/users


Print out:

    - the status code
    - the encoding of the response
    - the text of the response body
'''

# https://api.coingecko.com/api/v3  --> for coingecko application; wallet calculator


import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

print("--------------")
print("Status code: ", response.status_code)
print("--------------")
print("Encoding: ", response.encoding)
print("--------------")
print("Content:"), pprint(response.content)
'''
test_url = "https://api.coingecko.com/api/v3"
response_coin = requests.get(test_url)
print(response_coin.status_code)  # --> 404 bad request
'''
