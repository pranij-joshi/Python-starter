#This program simulates a Bridge-Keeper charged with gaurding an important bridge from those on a quest.
#The bridge-keeper asks three questions and if they are answered incorrectly they are sent to the Gorge
#of eternal peril.

#the programs displays question by the bridge keeper and takes answers from the user. Then the program
#matches the answer given by the user to see if they can pass the bridge or be sent to eternal peril.


print()                                                                         #line break
print("Stop! Who would corss the Bridge of Death")                              #displays the message
print("Must answer me these questions three, 'ere the other side he see.")      #displays the message
print()                                                                         #line break

name = input("What is your name?")                                              #asks the  user for their name
if name.lower() == "arthur":                                                    #if the name is arthur condition
    print("My liege! You may pass.")                                            #displays message
else:                                                                           #when the name is not arthur
    quest = input("What is your quest?")                                        #asks the user for their quest
    if "grail" in quest.lower():                                                #if there is the word grail in his quest
        color = input("What is your favourite colour?")                         #asks the user for the color
        if name[0].lower() == color[0].lower():                                 #if the first letter of color and name matches
            print("You may pass.")                                              #displays the message
        else:                                                                   #if the letters dont match
            print("Incorrect! You must now face the Gorge of Eternal Peril.")   #prints the message
    else:
        print("Only those who seek the Grail may pass.")                        #if there is no grail in the quest