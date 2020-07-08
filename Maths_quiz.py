import random


# setting up a function that decorates all my statements
def decoration_statement(statement, char):
    print()
    print(char * len(statement))
    print(statement)
    print(char * len(statement))
    print()


# setting up a function that checks users response for the question whether they are in primary, secondary or high school
def item_check(question, to_check):
    valid = False
    while not valid:
        # asking a question and converting response into lowercase
        response = input(question).lower()
        # checking if response is whether a whole word (primary/secondary/high) or a first letter of the word (p/s/h)
        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item
        # printing an error
        print("Sorry, I don't understand")


# setting up a function that checks if user wrote a valid response
def response_check(question, compare=None, number=None, low=None):
    # initializing an error message
    error = ""
    # initializing an error message for checking if a number is an integer
    if compare is None and number is not None:
        # initializing an error message for checking if user entered an integer more than a certain number
        if low is not None:
            error = ("Please write an integer more than "
                     + str(low - 1))
        elif low is None:
            error = "Please write an integer"
    # initializing an error message for checking the comparing signs (<, > or =)
    elif compare is not None and number is None:
        error = "Please write <, > or ="

    if number is not None and compare is None:
        # checking if a number is an integer
        while True:
            try:
                print()
                response = int(input(question))
                # checking if user entered an integer more than a certain number
                if low is not None and response < low:
                    print(error)
                    continue
                return response
            except ValueError:
                print(error)
                continue
    elif compare is not None and number is None:
        # checking comparing signs (<, > or =)
        while True:
            print()
            response = input(question)
            if response == "<" or response == ">" or response == "=":
                return response
            else:
                print(error)
            continue

def dividing():
    numb1 = random.randrange(1, 20)
    numb2 = random.randrange(1, 20)
    while True:
        numb1 = random.randrange(1, 20)
        numb2 = random.randrange(1, 20)
        try:
            div = int(numb1 % numb2)
            continue
        except:
            print(numb1)
            print(numb2)
            return numb1, numb2

# setting up a function for the quiz for primary school children
def primary_quiz():
    global correct
    global wrong
    global users_ans
    global correct_ans
    # using a decoration_statement function to decorate a message
    decoration_statement("Part 1: Compare the given numbers (<,>,=):", "*")
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    # generating questions where user have to compare numbers (whether it's more, less or equal)
    for i in range(1, num_questions + 1):
        # randomly generating 2 numbers between 1 and 100
        num1 = random.randrange(1, 100)
        num2 = random.randrange(1, 100)
        users_ans = response_check("Question {}: {} _ {}\n".format(i, num1, num2), compare=1)
        if users_ans == "<" and num1 < num2:
            print("Correct")
            correct += 1
        elif users_ans == ">" and num1 > num2:
            print("Correct")
            correct += 1
        elif users_ans == "=" and num1 == num2:
            print("Correct")
            correct += 1
        else:
            print("Wrong")
            wrong += 1

    # using a decoration_statement function to decorate a message
    decoration_statement("Part 2: Adding and subtracting", "*")
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    for i in range(1, num_questions + 1):
        # randomly generating an action that we are going to do with the numbers (add or subtract)
        action = random.choice(add_sub)
        # adding
        if action == "add":
            # randomly generating 2 numbers between 1 and 50
            num1 = random.randrange(1, 50)
            num2 = random.randrange(1, 50)
            users_ans = response_check("Question {}: {} + {} = ?\n".format(i, num1, num2), number=1)
            correct_ans = num1 + num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # subtracting
        elif action == "subtract":
            # randomly generating 2 numbers between 1 and 50
            num1 = random.randrange(1, 50)
            num2 = random.randrange(1, 50)
            # checking that we are subtracting from a bigger number
            if num1 > num2:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num1, num2), number=1)
                correct_ans = num1 - num2
            else:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num2, num1), number=1)
                correct_ans = num2 - num1
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
    print()
    print("         Game summary")
    decoration_statement("Correct answers: {}".format(correct) + "  |  Wrong answers: {}".format(wrong), "%")


def secondary_quiz():
    global correct
    global wrong
    global users_ans
    global correct_ans
    # using a decoration_statement function to decorate a message
    decoration_statement("Part 1: Adding and subtracting", "-")
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    for i in range(1, num_questions + 1):
        # randomly generating an action that we are going to do with the numbers (add or subtract)
        action = random.choice(add_sub)
        # adding
        if action == "add":
            # randomly generating 2 numbers between 1 and 150
            num1 = random.randrange(1, 150)
            num2 = random.randrange(1, 150)
            users_ans = response_check("Question {}: {} + {} = ?\n".format(i, num1, num2), number=1)
            correct_ans = num1 + num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # subtracting
        elif action == "subtract":
            # randomly generating 2 numbers between 1 and 150
            num1 = random.randrange(1, 150)
            num2 = random.randrange(1, 150)
            # checking that we are subtracting from a bigger number
            if num1 > num2:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num1, num2), number=1)
                correct_ans = num1 - num2
            else:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num2, num1), number=1)
                correct_ans = num2 - num1
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1

    # using a decoration_statement function to decorate a message
    decoration_statement("Part 2: Multiplying and dividing", "-")
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    for i in range(1, num_questions + 1):
        # randomly generating an action that we are going to do with the numbers (multiply or divide)
        action = random.choice(mul_div)
        # multiplying
        if action == "multiply":
            # randomly generating 2 numbers between 1 and 10
            num1 = random.randrange(1, 10)
            num2 = random.randrange(1, 10)
            users_ans = response_check("Question {}: {} * {} = ?\n".format(i, num1, num2), number=1)
            correct_ans = num1 * num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # dividing
        elif action == "divide":
            num1, num2 = dividing()
            print(num1)
            print(num2)
            '''users_ans = response_check("Question {}: {} / {} = ?\n".format(i, num1, num2), number=1)
            correct_ans = num1 / num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1'''


def high_quiz():
    print("web")


# initializing variables
correct = 0
wrong = 0
users_ans = 0
correct_ans = 0
# creating a list to check words primary, secondary or high
psh = ["primary", "secondary", "high"]
# creating a list to randomly generate an action
mul_div = ["multiply", "divide"]
# creating list to randomly generate an action
add_sub = ["add", "subtract"]
# asking user whether they are in primary, secondary or high school and checking their response
users_school_year = item_check("Are you in primary (p), secondary (s) or high (h) school? ", psh)
print(users_school_year)
if users_school_year == "primary":
    primary_quiz()
elif users_school_year == "secondary":
    secondary_quiz()
else:
    high_quiz()
