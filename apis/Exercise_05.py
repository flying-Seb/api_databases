'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''























'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

# id's to delete: 79,80,81


# maybe create a for loop
delete_to_server_79 = requests.delete(url + "/79")
delete_to_server_80 = requests.delete(url + "/80")
delete_to_server_81 = requests.delete(url + "/81")

print(delete_to_server_79.status_code)
print(delete_to_server_80.status_code)
print(delete_to_server_81.status_code)

# works several times but after running one times there are no elements with this id's anymore?!
'''