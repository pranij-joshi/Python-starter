from random import choice
from re import search


# extracts the username from email and returns it.
def get_user(mail):

    user = ""                 # creates an empty string
    for x in mail:            # for loop to go through mail
        if x == "@":          # breaks the loop if "@" is found in the string
            break
        user += x             # adds the characters to the user

    return user               # returns the user


# asks user for input and returns the user and the email
def get_email():

    while True:               # loop runs continuously until break
        mail = input("Please enter your Poppleton email address: ")     # asks the user for the email input
        count = 0             # declaring variable count set to 0
        for x in mail:        # for loop goes through the characters in mail
            if x == "@":      # if the characters in mail is '@'
                count += 1    # count is incremented by 1

        # if the mail satisfies the conditions then the loop breaks
        if mail != "" and mail[0] != "@" and mail[1] != "@" and count == 1 and "@pop.ac.uk" in mail and search("@pop.ac.uk$", mail):
            break

        # message for invalid email
        print("Invalid email. Please try again.")

    return mail             # returns the mail

# function takes in the question as argument.
def answers(questions):

    # list of output if the questions asked is unknown
    unknown = ["Hmmm", "Oh, yes, I see", "Tell me more", "I didn't quite get it", "This is interesting"]


    if "LIBRARY" in questions.upper():                                      # if the word "LIBRARY" is in user input
        print("The Library is closed today.")
    elif "LUNCH" in questions.upper():                                      # if the word "LUNCH" is in user input
        print("The cafeteria is open till 9 p.m.")
    elif "WIFI" in questions.upper():                                       # if the word "WIFI" is in user input
        print("WiFi is excellent across campus.")
    elif "DEADLINE" in questions.upper():                                   # if the word "DEADLINE" is in user input
        print("Your deadline has been extended by two working days.")
    elif "COFFEE" in questions.upper():                                     # if the word "COFFEE" is in user input
        print("The coffee shop is open till 9 p.m.")
    elif "YES" in questions.upper():                                        # if the word "Yes" is in user input
        print("Yes?")
    elif "HELLO" in questions.upper():                                      # if the word "HELLO" is in user input
        print("Hello.")
    else:                                                                   # if the words are unknown in user input
        print(choice(unknown))                                              # prints a random choice from unknown list

# list of names of the AI
name = ["Jarvis", "Friday", "Edith", "Karen"]

# prints the welcome message
print("Welcome to Pop chat\nOne of our operator will be pleased to help you today\n")

# calls the get_mail function and gives the value to email
email = get_email()

# calls the get_user function with email as argument and gives the value to user
user = get_user(email)

# printing the message
print("Hi,", user,"! Thank you, and Welcome to PopChat!")
print("My name is", choice(name), ", and it will be my pleasure to help you.")

# words to end the program
end = ["bye", "exit", "", "done", "end", "help", "quit"]

# creating a list l with elements in range from 0 - 10
l = [x for x in range(1, 11)]

temp = choice(l)        # random element is chosen from the list l

if temp == 1:           # if temp is 1 then it shows network error
    print("***Network Error***")

else:                   # if temp is not 1 then the program runs
    while True:

        questions = input("---->")          # takes input form the user
        if questions.lower() in end:        # if the user input has end words in it the loop breaks
            break
        answers(questions)                  # calls the answers function

# prints the end message
print("\n\nThanks,", user, ", for using PopChat. See you again soon!")

