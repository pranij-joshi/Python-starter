e = [] # creating an empty list to store the speed in KPH
u = [] # creating an empty list to store the speed in MPH

# takes input from the user for speed
speed = input("Enter the Reading: ")

# condition if the speed entered in null
if speed == "":
    print("No reading entered. Nothing to do.")

# else condition if any input is taken
else:
    # loop runs unless a null entry is recorded
    while True:

        # if the speed is null the loop breaks
        if speed == "":
            break

        # condition if the speed is entered in KPH
        elif speed[0].upper() == "E":
            print("Reading saved")

            e.append(float(speed[1:]))              # appends the value in the 'e' list
            u.append(float(speed[1:])/1.61)         # changes the KPH to MPH and Appends the value in the 'u' list

        elif speed[0].upper() == "U":
            print("Reading saved")
            u.append(float(speed[1:]))              # appends the value in the 'u' list
            e.append(float(speed[1:])*1.61)         # changes the MPH to KPH and appends the value in the 'e' list

        else:
            print("Unidentified value")             # if the value entered doesn't have an 'E' or "U'
            print("Enter a valid value")

        speed = input("Enter the Next Reading: ")   # asks the user for the another reading.


if e != []:                                             # if the list is not empty
    print("\n")                                         # for line break
    print("The values in entered order in KPH are: ")
    for x in e:                                         # for loop to print the values in 'e' list
        print(x, end="  ")


    print("\n")                                         # for line break
    print("The values in entered order in MPH are: ")
    for x in u:                                         # for loop to print the values in 'u' list
        print(x, end="  ")

    temp1 = sorted(e)                                   # temporary list to store the sorted 'e' list
    temp2 = sorted(u)                                   # temporary list to store the sorted 'u' list

    print("\n")                                         # line break
    print("Results Summary")
    print()                                             # line break
    print(len(u),"Reading analysed")
    print()                                             # line break
    print(f"Max Speed:\t {temp1[len(temp1)-1]:6.1f} KPH, {temp2[len(temp2)-1]:6.1f} MPH")       # displays the max speed in KPH and MPH
    print(f"Min Speed:\t {temp1[0]:6.1f} KPH, {temp2[0]:6.1f} MPH")                             # displays the min speed in KPH and MPH

    total = 0                                          # total variable set to 0.

    for x in e:                                         # for loop to add the valus in the list 'e'
        total += x

    average = total/len(e)                              # calculates the average of values in list 'e'
    print(f"Avg Speed:\t {average:6.1f} KPH, {average/1.61:6.1f} MPH")      # print the average speed in KPH and MPH`