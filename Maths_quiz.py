import random


# setting up a function that decorates all my statements
def decoration_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


def item_check():
    global users_school_year

    users_school_year = input("Are you in primary (p), secondary (s) or high (h) school? ")
    if users_school_year.lower() == "primary" or users_school_year.lower() == "p":
        users_school_year = "primary"
    elif users_school_year.lower() == "secondary" or users_school_year.lower() == "s":
        users_school_year = "secondary"
    elif users_school_year.lower() == "high" or users_school_year.lower() == "h":
        users_school_year = "high"
    else:
        print("Sorry, I don't understand")
        print()
        # run this function to ask user again
        item_check()
    return users_school_year

for i in [1,5]:
    users_school_year = item_check()
    print(users_school_year)
