from random import choice

#asks user for input and returns the user and the email
def check_email():

    mail = input("Please enter your Poppleton email address: ")
    if "@" in mail or len(mail) < 3:
        return "E", "E"
    else:
        return mail, mail+"@pop.ac.uk"


def answers(questions):

    unknown = ["Hmmm", "Oh, yes, I see", "Tell me more", "I didn't quite get it", "This is interesting"]


    if "LIBRARY" in questions.upper():
        print("The Library is closed today.")
    elif ("HELLO" or "HI") in questions.upper():
        print("Hello.")
    elif ("CAFETERIA" or "LUNCH" or "FOOD") in questions.upper():
        print("The cafeteria is open till 9 p.m.")
    elif "WIFI" in questions.upper():
        print("WiFi is excellent across campus.")
    elif "DEADLINE" in questions.upper():
        print("Your deadline has been extended by two working days.")
    elif "COFFEE" in questions.upper():
        print("The coffee shop is open till 9 p.m.")
    elif "YES" in questions.upper():
        print("Yes?")
    else:
        print(choice(unknown))
name = ["Peter Parker", "Tony Stark", "Bruce Banner", "Clark Kent", "Bruce Banner", "Barry Allen", "Steve Rogers"]

print("Welcome to Pop chat\nOne of our operator will be pleased to help you today\n")

user, email = check_email()


if user != "E":
    print("Hi,", user,"! Thank you, and Welcome to PopChat!")
    print("My name is", choice(name), ", and it will be my pleasure to help you.")

    end = ["bye", "exit", "", "done", "end", "help", "quit"]

    l = [x for x in range(1, 11)]

    temp = choice(l)

    if temp == 1:
        print("***Network Error***")

    else:
        while True:

            questions = input("---->")
            if questions.lower() in end:
                break
            answers(questions)

    print("\n\nThanks,", user, ", for using PopChat. See you again soon!")

else:
    print("ERROR")