'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''





























'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

server_response = requests.get(url).json()

email_adresses = []

# ask Johnny how to do this (in a shorter form)?
for user in server_response["data"]:
    user_email = user['email']  # you have to access the emails by entering every user directly
    # wrong way:
    # user_email = server_response['data'][user]['email']
    email_adresses.append(user_email)


pprint(email_adresses)
'''

