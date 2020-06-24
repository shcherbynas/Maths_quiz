import random


# setting up a function that decorates all my statements
def decoration_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


def item_check(question, to_check):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Sorry, I don't understand")


# setting a function that checks if user wrote a valid response
def response_check(question, compare=None, number=None, low=None):
    global error
    if compare is None and number is not None:
        if low is not None:
            error = ("Please write an integer more than "
                     + str(low - 1))
        elif low is None:
            error = ("Please write an integer")
    elif compare is not None and number is None:
        error = ("Please write <, > or =")

    if number is not None and compare is None:
        while True:
            try:
                print()
                response = int(input(question))
                if low is not None and response < low:
                    print(error)
                    continue
                return response
            except ValueError:
                print(error)
                continue
    elif compare is not None and number is None:
        while True:
                print()
                response = input(question)
                if response == "<" or response == ">" or response == "=":
                    return response
                else:
                    print(error)
                continue


def primary_quiz():
    decoration_statement("Part 1: Compare these numbers (<,>,=):", "*")
    for i in range(1, 6):
        num1 = random.randrange(1, 100)
        num2 = random.randrange(1, 100)
        users_answer = response_check("Question {}: {} _ {}\n".format(i, num1, num2), compare=1)
        if users_answer == "<" and num1 < num2:
            print("Correct")
        elif users_answer == ">" and num1 > num2:
            print("Correct")
        elif users_answer == "=" and num1 == num2:
            print("Correct")
        else:
            print("wrong")

    decoration_statement("Part 2: ", "*")

def secondary_quiz():
    print("jreg")

def high_quiz():
    print("web")


psh = ["primary", "secondary", "high"]
users_school_year = item_check("Are you in primary (p), secondary (s) or high (h) school? ", psh)
print(users_school_year)
if users_school_year == "primary":
    primary_quiz()
elif users_school_year == "secondary":
    secondary_quiz()
else:
    high_quiz()
