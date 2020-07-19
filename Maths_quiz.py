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
        # checking if user's response is correct
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
            # randomly generating 2 numbers between 1 and 20
            num1 = random.randrange(1, 20)
            num2 = random.randrange(1, 20)
            users_ans = response_check("Question {}: {} + {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's response is correct
            correct_ans = num1 + num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # subtracting
        elif action == "subtract":
            # randomly generating 2 numbers between 1 and 20
            num1 = random.randrange(1, 20)
            num2 = random.randrange(1, 20)
            # checking that we are subtracting from a bigger number
            if num1 > num2:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num1, num2), number=1)
                # calculating correct answer
                correct_ans = num1 - num2
            else:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num2, num1), number=1)
                # calculating correct answer
                correct_ans = num2 - num1
            # checking if user's response is correct
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
    print()
    print("         Game summary")
    decoration_statement("Correct answers: {}".format(correct) + "  |  Wrong answers: {}".format(wrong), "%")


# setting up a function for the quiz for secondary school children
def secondary_quiz():
    global correct, wrong
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
            # randomly generating 2 numbers between 1 and 100
            num1 = random.randrange(1, 100)
            num2 = random.randrange(1, 100)
            users_ans = response_check("Question {}: {} + {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's response is correct
            correct_ans = num1 + num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # subtracting
        elif action == "subtract":
            # randomly generating 2 numbers between 1 and 100
            num1 = random.randrange(1, 100)
            num2 = random.randrange(1, 100)
            # checking that we are subtracting from a bigger number
            if num1 > num2:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num1, num2), number=1)
                # calculating correct answer
                correct_ans = num1 - num2
            else:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num2, num1), number=1)
                # calculating correct answer
                correct_ans = num2 - num1
            # checking if user's response is correct
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
            # asking a question
            users_ans = response_check("Question {}: {} * {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's answer is correct
            correct_ans = num1 * num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # dividing
        elif action == "divide":
            # randomly generating a number between 0 and 20
            num1 = random.randrange(0, 20)
            # creating list to randomly generate a number for division, that includes only 1 and the number that we are dividing
            div = [1, num1]
            # if this number can be divided by 4 with a remainder 0, it will be divided by 1, 2, 4 or the number itself
            if num1 % 4 == 0:
                div.append("2")
                div.append("4")
                num2 = random.choice(div)
            # if the first number can be divided by 3 with a remainder 0, it will be divided by 1, 3 or the number itself
            elif num1 % 3 == 0:
                div.append("3")
                num2 = random.choice(div)
            # if the first number can't be divided by 4 or 3, it will be divided by 1 or the number itself
            else:
                num2 = random.choice(div)
            # asking a question
            users_ans = response_check("Question {}: {} / {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's response is correct
            correct_ans = num1 / int(num2)
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
    print()
    print("         Game summary")
    decoration_statement("Correct answers: {}".format(correct) + "  |  Wrong answers: {}".format(wrong), "%")


# setting up a function for the quiz for high school children
def high_quiz():
    global correct, wrong
    global users_ans
    global correct_ans
    # using a decoration_statement function to decorate a message
    decoration_statement("Part 1: Adding and subtracting", "-")
    # asking user if they would like to include negative numbers
    negative = item_check("Would like to include to include negative numbers? (yes/no) ", yes_no)
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    for i in range(1, num_questions + 1):
        # randomly generating an action that we are going to do with the numbers (add or subtract)
        action = random.choice(add_sub)
        # if user said to include negative numbers, generating numbers between -50 and 200, if not - between 0 and 500
        if negative == "yes":
            # randomly generating 2 numbers between -50 and 200
            num1 = random.randrange(-50, 150)
            num2 = random.randrange(-50, 150)
        else:
            # randomly generating 2 numbers between 0 and 500
            num1 = random.randrange(0, 200)
            num2 = random.randrange(0, 200)
        # adding
        if action == "add":
            users_ans = response_check("Question {}: {} + {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's response is correct
            correct_ans = num1 + num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # subtracting
        elif action == "subtract":
            # checking that we are subtracting from a bigger number
            if num1 > num2:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num1, num2), number=1)
                # calculating correct answer
                correct_ans = num1 - num2
            else:
                users_ans = response_check("Question {}: {} - {} = ?\n".format(i, num2, num1), number=1)
                # calculating correct answer
                correct_ans = num2 - num1
            # checking if user's response is correct
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1

    # using a decoration_statement function to decorate a message
    decoration_statement("Part 2: Multiplying and dividing", "-")
    # asking user if they would like to include negative numbers
    negative = item_check("Would like to include to include negative numbers? (yes/no) ", yes_no)
    # asking user how many questions do they want to have in this part
    num_questions = response_check("How many questions do you want to have? ", number=1, low=1)
    for i in range(1, num_questions + 1):
        # randomly generating an action that we are going to do with the numbers (multiply or divide)
        action = random.choice(mul_div)
        # multiplying
        if action == "multiply":
            # if user said to include negative numbers, generating numbers between -10 and 15, if not - between 0 and 20
            if negative == "yes":
                # randomly generating 2 numbers between -10 and 15
                num1 = random.randrange(-10, 15)
                num2 = random.randrange(-10, 15)
            else:
                # randomly generating 2 numbers between 0 and 20
                num1 = random.randrange(0, 20)
                num2 = random.randrange(0, 20)
            # asking a question
            users_ans = response_check("Question {}: {} * {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's answer is correct
            correct_ans = num1 * num2
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
        # dividing
        elif action == "divide":
            # if user said to include negative numbers, generating a number between -10 and 20, if not - between 0 and 50
            if negative == "yes":
                # randomly generating a number between -10 and 20
                num1 = random.randrange(-10, 20)
            else:
                # randomly generating a number between 0 and 50
                num1 = random.randrange(0, 50)
            # creating list to randomly generate a number for division, that includes only 1 and the number that we are dividing
            div = [1, num1]
            # if this number can be divided by 4 with a remainder 0, it will be divided by 1, 2, 4 or the number itself
            if num1 % 4 == 0:
                div.append("2")
                div.append("4")
                num2 = random.choice(div)
            # if the first number can be divided by 3 with a remainder 0, it will be divided by 1, 3 or the number itself
            elif num1 % 3 == 0:
                div.append("3")
                num2 = random.choice(div)
            # if the first number can't be divided by 4 or 3, it will be divided by 1 or the number itself
            else:
                num2 = random.choice(div)
            # asking a question
            users_ans = response_check("Question {}: {} / {} = ?\n".format(i, num1, num2), number=1)
            # calculating correct answer and checking if user's response is correct
            correct_ans = num1 / int(num2)
            if users_ans == correct_ans:
                print("Correct")
                correct += 1
            else:
                print("Wrong, answer is {}".format(correct_ans))
                wrong += 1
    print()
    print("         Game summary")
    decoration_statement("Correct answers: {}".format(correct) + "  |  Wrong answers: {}".format(wrong), "%")


# introduction, rules
print()
decoration_statement("    Welcome to the Maths quiz    ", "<")
print("This is a maths quiz for school kids of different ages.")
print("At the beginning of the quiz you have to state whether you are in primary, secondary or high school")
print("(there will be different questions depending on your age).")
print("There are two parts of the quiz (each one directed on a particular subject in maths).")
print("In each part you can choose how many questions you want to be asked.")
print("At the end you will see how many correct and wrong answers you got.")
print()
print("Let's start! Good luck!")
print()

# initializing variables
correct = 0
wrong = 0
users_ans = 0
correct_ans = 0

# creating a list to check words primary, secondary or high
psh = ["primary", "secondary", "high"]
# creating a list to check words yes or no
yes_no = ["yes", "no"]
# creating a list to randomly generate an action
mul_div = ["multiply", "divide"]
# creating list to randomly generate an action
add_sub = ["add", "subtract"]
# creating a variable 'keep_going' for being able to continue or quit the game

keep_going = ""
while keep_going == "":
    # asking user whether they are in primary, secondary or high school and checking their response
    users_school_year = item_check("Are you in primary (p), secondary (s) or high (h) school? ", psh)
    if users_school_year == "primary":
        primary_quiz()
    elif users_school_year == "secondary":
        secondary_quiz()
    else:
        high_quiz()
    # asking user if they want to continue playing
    keep_going = input("Press <enter> to do the quiz one more time or any other key to finish ")
else:
    print("Game finished. Thank you for playing!")
