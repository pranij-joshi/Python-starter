"""Program to make a technical support system, based on an interactive online chat."""

from random import choice  # Imports only 'choice' function from the module 'random'.

operator_name = ["Aaron", "Caroline", "Arthur", "Janice", "Alicia", "Fiona", "Jack"]
random_answers = ["Hmm", "Oh yes, I see", "Tell me more"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
program_exit = ["", " ", "BYE", "END", "QUIT", "EXIT", "HELP"]

print("""\nWelcome to Pop Chat
One of our operators will be pleased to help you today.\n""")  # Triple quote statement across multiple lines.


def email_verification():
    while True:
        count = 0
        user_email = input("Please enter your Poppleton email address: ")

        for y in user_email:
            if y == "@":
                count += 1
        if len(user_email) >= 12 and count == 1 and "@pop.ac.uk" in user_email:
            break
        else:
            print("Please input a valid email address with the domain pop.ac.uk.")
    return user_email


def solutions(user_questions):
    if "HI" in user_questions.upper():
        print("Hello, how may I help you?")
    elif "WIFI" in user_questions.upper():
        print("WiFi is excellent across the campus.")
    elif "LIBRARY" in user_questions.upper():
        print("The library is closed today.")
    elif "BOOK" in user_questions.upper():
        print("You can visit the library on working hours to get the book.")
    elif "CAFETERIA" in user_questions.upper():
        print("The cafeteria is open till 9 p.m.")
    elif "LUNCH" in user_questions.upper():
        print("The cafeteria is open till 9 p.m.")
    elif "COFFEE" in user_questions.upper():
        print("Teekee is open until 9 pm this evening.")
    elif "DEADLINE" in user_questions.upper():
        print("Your deadline has been extended by two working days.")
    elif "YES" in user_questions.upper():
        print("Yes?")
    elif "" in user_questions.upper():
        print("\nThanks,", user, ", for using PopChat. See you again soon!")
    elif " " in user_questions.upper():
        print("\nThanks,", user, ", for using PopChat. See you again soon!")
    else:
        print(choice(random_answers))


email = email_verification()
user = email.split("@")[0]

print("Hi,", user, "! Thank you, and Welcome to PopChat!")
print("My name is", choice(operator_name), ", and it will be my pleasure to help you.")

x = choice(numbers)
if x == 3:
    print("*** NETWORK ERROR ***")
else:
    while True:
        user_questions = input("--->")
        if user_questions.upper() in program_exit:
            break
        solutions(user_questions)

print("\nThanks,", user, ", for using PopChat. See you again soon!")
