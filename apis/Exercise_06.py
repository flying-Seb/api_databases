'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

import requests
from pprint import pprint

users_url = "http://demo.codingnomads.co:8080/tasks_api/users"
tasks_url = "http://demo.codingnomads.co:8080/tasks_api/tasks"


def main():
    '''A function to setup the menu for the user and print the options to the screen'''

    print(
        "----------------------------------------\n"
        "------------------------\n"
        "----------\n"
        "Please select from the following options (enter the number of the action you would like to take): \n"        
        "----------\n"
        "------------------------\n"
        "----------------------------------------\n"
        "\n"
        "1) Create a new account\n"
        "2) View all your tasks\n"
        "3) View your completed tasks\n"
        "4) View only your incomplete tasks\n"
        "5) Create a new task\n"
        "6) Update an existing task\n"
        "7) Delete a task\n"
    )
    user_input = int(input("What do you want to do? --> "))  # strings throw an error right here!
    verify_input(user_input)

    if user_input == 1:
        create_account_1()
    elif user_input == 2:
        view_all_tasks_2()
    elif user_input == 3:
        view_completed_tasks_3()
    elif user_input == 4:
        view_incomplete_tasks_4()
    elif user_input == 5:
        pass
    elif user_input == 6:
        pass
    elif user_input == 7:
        pass
    else:
        print("Whooops! Something went terribly wrong!")
    return


def verify_input(user_input):  # what do I do with strings??
    '''A function to verify that the user entered a correct number of the menu'''

    try:
        if 0 < user_input < 8:
            "----------------------------------------\n"
            print("Thank you for your input!")
        else:
            print("There has been a mistake. Please enter a number from the menu: ")
            main()
    except ValueError:
        print("Please enter a number from the menu.")


def verify_byebye(user_input):
    '''A function to verify the input to proceed or exit the app'''

    try:
        if user_input.lower() == 'm':
            main()
        elif user_input.lower() == 'e':
            print("See you next time! Bye bye...")
    except ValueError:
        print("That is not what I expected. Please try again.")
        question_afterwards()


def create_account_1():
    '''A function for the first point of the menu'''

    print("----------------------------------------\n")
    print("You want to create a new account. Therefore we need your first name, last name \n"
          "and your email.")
    print("----------------------------------------\n")
    user_first = str(input("Please enter your first name: --> "))
    user_last = str(input("Please enter your last name: --> "))
    user_mail = str(input("Please enter your email: --> "))

    body = {
        'first_name': f"{user_first}",
        'last_name': f"{user_last}",
        'email': f"{user_mail}"
    }

    response = requests.post(users_url, json=body)

    print(f"Response status code: {response.status_code} \n"
          f"New user has successfully been created!")

    question_afterwards()


def view_all_tasks_2():
    '''A function to view all tasks'''

    print("----------------------------------------\n")
    print("You want to see all your tasks. Therefore we need your UserId.")
    print("----------------------------------------\n")
    userId_input = input("Please enter your UserId: --> ")

    # to see all tasks of a user the url has to be the user_url/userId/tasks
    url_add_on = f"/{userId_input}/tasks?complete=-1"

    response = requests.get(users_url + url_add_on)
    tasks = response.json()
    pprint(tasks)

    question_afterwards()


def view_completed_tasks_3():
    '''A function to view the completed tasks'''

    print("----------------------------------------\n")
    print("You want to see your completed tasks. Therefore we need your UserId.")
    print("----------------------------------------\n")
    userId_input = input("Please enter your UserId: --> ")

    # to see all tasks of a user the url has to be the user_url/userId/tasks
    url_add_on = f"/{userId_input}/tasks?complete=true"

    response = requests.get(users_url + url_add_on)
    tasks = response.json()
    pprint(tasks)

    question_afterwards()


def view_incomplete_tasks_4():
    '''A function to view the incompleted tasks'''

    print("----------------------------------------\n")
    print("You want to see your completed tasks. Therefore we need your UserId.")
    print("----------------------------------------\n")
    userId_input = input("Please enter your UserId: --> ")

    # to see all tasks of a user the url has to be the user_url/userId/tasks
    url_add_on = f"/{userId_input}/tasks?complete=false"

    response = requests.get(users_url + url_add_on)
    tasks = response.json()
    pprint(tasks)

    question_afterwards()


def create_new_task_5():
    pass


def update_task_6():
    pass


def delete_task_7():
    pass


def question_afterwards():
    '''This is a function to ask the user if he wants to do something else or exit the app after one task'''

    print("----------------------------------------\n")
    print("You have been served. Do you want to do anything else? \n"
          "Please enter the character of your option to proceed: ")
    print("Decide what to do: \n"
          "* [M]enu \n"
          "* [E]xit")

    user_input = input("Your input: --> ")

    verify_byebye(user_input)


main()