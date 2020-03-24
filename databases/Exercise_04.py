'''

Please create a new Python application that interfaces with a brand new database.
This application must demonstrate the ability to:

    - create at least 3 tables
    - insert data to each table
    - update data in each table
    - select data from each table
    - delete data from each table
    - use at least one join in a select query

BONUS: Make this application something that a user can interact with from the CLI. Have options
to let the user decide what tables are going to be created, or what data is going to be inserted.
The more dynamic the application, the better!

'''

# maybe work with args* and kwargs** as an input from the user to make the tables more individual
# do that in the capstone! and use django as well in the capstone!

import sqlalchemy
import pymysql
from pprint import pprint

def main():
    '''controller for the application'''
    create_engine_0()
    menu_action()


# done
def create_engine_0():
    '''Create the engine to connect to the database'''

    global engine
    engine = sqlalchemy.create_engine('mysql+pymysql://user:pw@localhost/SocialDB')
    global connection
    connection = engine.connect()
    global metadata
    metadata = sqlalchemy.MetaData()
    return engine, connection, metadata


# done
def menu_action():
    """A function for the menu and the program logic"""

    print(
        "----------------------------------------\n"
        "Hello there! Thank you for using my application. This application was created that you can \n"
        "create tables and insert, update and delete data from and to the SocialDB. Below you can find the menu \n"
        "for further actions. \n"
        "\n"
        "Please select from the following options (enter the number of the action you would like to take): \n"
        "----------------------------------------\n"
        "------------------------\n"
        "----------\n"
        "-----\n"
        "\n"
        "\n"
        "1) Create a new table\n"
        "\n"
        "2) Insert data in a table of your choice\n"
        "\n"
        "3) Update data in a table\n"
        "\n"
        "4) Select all data from a table\n"
        "\n"
        "5) Delete data from a table\n"
        "\n"
        "6) Exit the application\n"
        "\n"
    )
    user_input = int(input("What do you want to do? --> "))  # strings throw an error right here!
    "\n"
    verify_input(user_input)

    if user_input == 1:
        create_table_1()
    elif user_input == 2:
        insert_data_2()
    elif user_input == 3:
        update_data_3()
    elif user_input == 4:
        select_data_4()
    elif user_input == 5:
        delete_data_5()
    elif user_input == 6:
        exit_app_6()
    else:
        print("Whooops! Something went terribly wrong!")
    return


# done
def verify_input(user_input):  # still don't know what to do with strings!
    """A function to verify that the user input is a correct number of the menu"""

    try:
        if 0 < user_input < 7:
            "----------------------------------------\n"
            "\n"
            print("Thank you for your input!")
            "\n"
        else:
            "\n"
            print("There has been a mistake. Please enter a number from the menu. ")
            "\n"
            main()
    except ValueError:
        "\n"
        print("Please enter a number from the menu.")
        "\n"


# done
def verify_byebye(user_input):
    """A function to verify the input to proceed or exit the app"""

    try:
        if user_input.lower() == 'm':
            menu_action()
        elif user_input.lower() == 'e':
            exit_app_6()
    except ValueError:
        "\n"
        print("That is not what I expected. Please try again.")
        "\n"
        question_afterwards()


# done
def question_afterwards():
    """This is a function to ask the user if he wants to do something else or exit the app after one task"""

    print("----------------------------------------\n")
    "\n"
    print("You have been served. Do you want to do anything else? \n"
          "Please enter the character of your option to proceed: ")
    "\n"
    print("Decide what to do: \n"
          "\n"
          "* [M]enu \n"
          "\n"
          "* [E]xit")
    "\n"

    user_input = input("Your input: --> ")
    "\n"
    verify_byebye(user_input)


# bug fixxing regarding the "table already exists issue"!
def create_table_1():
    """A function to create a table in the new SocialDB"""
    try:
        user_input = input("Name the table you want to create: ")
        user_table = user_input

        # name the columns of the table
        user_col1 = input("Your table has one 'ID' column. The other columns you can choose yourself. \n"
                          "Please enter the second column your table should have: ")
        us_type1 = input("Should it be a [s]tring or an [i]nteger? ")
        "\n"
        user_col2 = input("Now enter the third column your table should have: ")
        us_type2 = input("Should it be a [s]tring or an [i]nteger? ")
        "\n"
        user_col3 = input("Now enter the last column your table should have: ")
        us_type3 = input("Should it be a [s]tring or an [i]nteger? ")

        # build the table statement column by column
        def build_column(user_statement):
            """ A function to determine if the user wants a column to be a string or an integer column.
            Therefore the sql alchemy query has to be changed depending on what the user wants"""

            global i  # to access it from outside
            if user_statement == 's':
                i = sqlalchemy.String(255)
            elif user_statement == 'i':
                i = sqlalchemy.Integer()
            else:
                print("Please try again.")
                create_table_1()
            return i

        newTable = sqlalchemy.Table(user_table, metadata,
                                    sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
                                    sqlalchemy.Column(user_col1, build_column(us_type1)),
                                    sqlalchemy.Column(user_col2, build_column(us_type2)),
                                    sqlalchemy.Column(user_col3, build_column(us_type3)),
                                    )
        metadata.create_all(engine)

        # since create_all checks if a table already exists you don't have to check that separately
        question_afterwards()
    except:
        print("This table already exists. Please try again.")
        menu_action()


# done
def insert_data_2():
    """A function to insert data in a table"""

    user_insert = input("You want to insert data in a table. In which table you want to insert in? ")
    "\n"
    print("See the columns of your chosen table: ")
    "\n"
    # build table object for the table to insert (create first, loop second)
    newTable = sqlalchemy.Table(user_insert, metadata, autoload=True, autoload_with=engine)
    # create_all(engine) to actually use newTable
    metadata.create_all(engine)
    # loop trough the columns to show the user where to insert data to
    for c in newTable.columns:
        print(f'* {c}')
        "\n"
    user_col1 = input("Please enter the value for the first column: ")
    user_col2 = input("Please enter the value for the second column: ")
    user_col3 = input("Please enter the value for the third column: ")
    user_col4 = input("Please enter the value for the fourth column: ")

    query = sqlalchemy.insert(newTable).values(Id=user_col1, first=user_col2, last=user_col3, friends=user_col4)

    # result_proxy to execute the query
    result_proxy = connection.execute(query)

    question_afterwards()
    return


# done
def update_data_3():
    """A function to update data in a table"""

    user_insert = input("You want to update data in a table. What table you want to update? ")
    "\n"
    print("See the columns of your chosen table: ")
    "\n"
    # build table object for the table to insert (create first, loop second)
    newTable = sqlalchemy.Table(user_insert, metadata, autoload=True, autoload_with=engine)
    # create_all(engine) to actually use newTable
    metadata.create_all(engine)
    # loop trough the columns to show the user where to update the data
    for c in newTable.columns:
        print(f'* {c}')

    user_insert = input("What ID do you want to update? ")
    "\n"
    print("Thanks for your input. Please enter the new values. ")
    user_val1 = input("Please enter the new value for the second column: ")
    user_val2 = input("Please enter the new value for the third column: ")
    user_val3 = input("Please enter the new value for the fourth column: ")

    query = sqlalchemy.update(newTable).values(first=user_val1, last=user_val2, friends=user_val3).where\
            (newTable.columns.Id == user_insert)
    result_proxy = connection.execute(query)
    question_afterwards()
    return


# done
def select_data_4():
    """A function to select data from a table"""

    user_table = input("What table to do you want to select data from? ")
    newTable = sqlalchemy.Table(user_table, metadata, autoload=True, autoload_with=engine)
    # print the columns in one string
    col_all = ""
    columns_user_table = [c for c in newTable.columns]
    for col in columns_user_table:
        col_all = col_all + f"{col}, "
    # remove the last space and comma from the string
    col_all = col_all[:-2]
    print(f"The columns of the table {user_table} are:" )
    print(col_all)

    query = sqlalchemy.select([newTable])
    result_proxy = connection.execute(query)
    result = result_proxy.fetchall()
    for item in result:
        print(item)

    question_afterwards()
    return


# done
def delete_data_5():
    """A function to delete data from a table"""

    print("You want to delete all data from a table. Here is a list with all the tables in the SocialDatabase: ")
    tables = engine.table_names()
    for table in tables:
        print(f"* {table}")
    "\n"
    user_input = input("Please name the table you want to delete: ")

    newTable = sqlalchemy.Table(user_input, metadata, autoload=True, autoload_with=engine)

    query = sqlalchemy.delete(newTable)

    result = connection.execute(query)

    question_afterwards()
    return


# done
def exit_app_6():
    """Function to quit"""
    print("See you next time! Bye bye...")


# set name to main if the program is called directly
if __name__ == '__main__':
    main()
