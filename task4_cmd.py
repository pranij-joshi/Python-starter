import sys

#creating a class Team
class Team:
    def __init__(self):
        """init function intializes all the values"""
        self.name = ""                                  # to save the team name
        self.p = 0                                      # to save the number of games played
        self.w = 0                                      # to save the number of wins
        self.d = 0                                      # to save the number of loss
        self.l = 0                                      # to save the number of draws
        self.f = 0                                      # to save the number of goals scored
        self.a = 0                                      # to save the number of goals conceded
        self.diff = 0                                   # to save the difference in goals
        self.pts = 0                                    # to save the points

    # set_name function takes name as argument and sets the team name
    def set_name(self, name):
        self.name = name

    # set_p function increases the games played by one everytime it is called
    def set_p(self):
        self.p += 1

    # set_p function increases the wins by one everytime it is called
    def set_w(self):
        self.w += 1

    # set_p function increases the draw by one everytime it is called
    def set_d(self):
        self.d += 1

    # set_p function increases the loss by one everytime it is called
    def set_l(self):
        self.l += 1

    # set_f function adds the goals scored by the team by taking an argument f
    def set_f(self, f):
        self.f += int(f)

    # set_f function adds the goals conceded by the team by taking an argument a
    def set_a(self, a):
        self.a += int(a)

    # calculate_diff function calculates the difference between the goals scored and conceded by the team
    def calculate_diff(self):
        self.diff = self.f - self.a

    # calculate_pts function calculates the points earned by the team
    def calculate_pts(self):
        self.pts = (int(self.w) * 3) + (int(self.d) * 1) + (int(self.l) * 0)

    # get_name function returns the name of the team
    def get_name(self):
        return self.name

    # get_name function returns the points of the team
    def get_pts(self):
        return self.pts

    # get_name function returns the goal difference of the team
    def get_diff(self):
        return self.diff

    # get_name function returns the goal scored of the team
    def get_f(self):
        return self.f

    # display function displays all the field of the team including the name
    def display(self):
        print(f"{self.name:15}{self.p:5}{self.w:5}{self.d:5}{self.l:5}{self.f:5}{self.a:5}{self.diff:8}{self.pts:7}")
        return ""

f = open("games.txt", "r")                              # opens the file for reading
lines = f.readlines()                                   # reads the content of the file and appends in the list lines
f.close()                                               # closes the file

team_names = set()                                      # creating an empty set as it doesn't support duplicate values

readings = []                                           # creating an empty list to store the required data
l_objects = []                                          # creating an empty list to store the list of objects


for x in lines:                                         # for loop goes through the elements in the list lines
    y = x.strip()                                       # strip() removes '\n' from the elements in the list
    readings.append(y.split(","))                       # splits the string at ',' and appends the reading list


for x in readings:                                      # for loop goes through the elements in the list reading
    team_names.add(x[0])                                # adds the 0 index element to the set team_names
    team_names.add(x[2])                                # adds the 2 index element to the set team_names


team_names = list(team_names)                           # changing the set team_name to list


for x in team_names:                                    # for loop goes through the elements in team_names list
    l_objects.append(Team())                            # appends an instance of Team class to the l_object list


count = 0                                               # creating count variable set to 0

for x in l_objects:                                     # for loop goes through the elements in the l_object list
    x.set_name(team_names[count])                       # sets the name from team_names list by calling the set_name function of Team class.
    count += 1                                          # incrementing count by 1


for x in readings:                                      # for loop to go through the elements in reading list
    if int(x[1]) > int(x[3]):                           # condition if the first team scored higher than the second team
        for y in l_objects:                             # for loop goes through the elements in the l_objects list
            if y.get_name() == x[0]:                    # if the name in the object matches the first team name
                y.set_p()                               # set_p function is called
                y.set_w()                               # set_w function is called
                y.set_f(x[1])                           # set_f function is called and the goal scored is passed as an argument
                y.set_a(x[3])                           # set_a function is called ane the goal conceded is passed as an argument

            if y.get_name() == x[2]:                    # if the name in the object matches the second team name
                y.set_p()                               # set_p function is called
                y.set_l()                               # set_l function is called
                y.set_f(x[3])                           # set_f function is called and the goal scored is passed as an argument
                y.set_a(x[1])                           # set_a function is called ane the goal conceded is passed as an argument

    elif int(x[1]) < int(x[3]):                         # condition if the second team scored higher than the first team
        for y in l_objects:                             # for loop goes through the elements in the l_objects list
            if y.get_name() == x[2]:                    # if the name in the object matches the second team name
                y.set_p()                               # set_p function is called
                y.set_w()                               # set_w function is called
                y.set_f(x[3])                           # set_f function is called and the goal scored is passed as an argument
                y.set_a(x[1])                           # set_a function is called ane the goal conceded is passed as an argument

            if y.get_name() == x[0]:                    # if the name in the object matches the first team name
                y.set_p()                               # set_p function is called
                y.set_l()                               # set_l function is called
                y.set_f(x[1])                           # set_f function is called and the goal scored is passed as an argument
                y.set_a(x[3])                           # set_a function is called ane the goal conceded is passed as an argument

    else:                                               # condition if both the teams scored equal goals
        for y in l_objects:
            if y.get_name() == x[0] or y.get_name() == x[2]:    # if the name in the object matches the first team name or the second team name
                y.set_p()                               # set_p function is called
                y.set_d()                               # set_d function is called
                y.set_f(x[1])                           # set_f function is called and the goal scored is passed as an argument
                y.set_a(x[1])                           # set_a function is called ane the goal conceded is passed as an argument


for x in l_objects:                                     # for loop goes through the elements in the l_objects list
    x.calculate_diff()                                  # calculate_diff function is called
    x.calculate_pts()                                   # calculate_pts function is called

temp = Team()                                           # creating a temporary instance for Team class
sort_table = False                                      # creating a variable giving it False value


while sort_table == False:                              # while loop runs until sort_table is True
    sort_table = True                                   # setting the sort_table value to True to break the loop
    for x in range(0, len(l_objects)-1):                # for loop goes through range of elements form 0 to len of l_object - 1
        if l_objects[x].get_pts() < l_objects[x+1].get_pts():           # it the points of first object is less than the second object
            temp = l_objects[x]                                         # temp object copies the value of first object
            l_objects[x] = l_objects[x+1]                               # first object copies the value of the second object
            l_objects[x+1] = temp                                       # second object copies the value of temp object
            sort_table = False                                          # sort_table set to False so that the loop continues to run

        elif l_objects[x].get_pts() == l_objects[x+1].get_pts():        # it the points of first object is equal the second object
            if l_objects[x].get_diff() < l_objects[x + 1].get_diff():   # it the goal difference of first object is less than the second object
                temp = l_objects[x]                                     # temp object copies the value of first object
                l_objects[x] = l_objects[x + 1]                         # first object copies the value of the second object
                l_objects[x + 1] = temp                                 # second object copies the value of temp object
                sort_table = False                                      # sort_table set to False so that the loop continues to run

            elif l_objects[x].get_diff() == l_objects[x + 1].get_diff():
                if l_objects[x].get_f() < l_objects[x + 1].get_f():
                    temp = l_objects[x]                                 # temp object copies the value of first object
                    l_objects[x] = l_objects[x + 1]                     # first object copies the value of the second object
                    l_objects[x + 1] = temp                             # second object copies the value of temp object
                    sort_table = False                                  # sort_table set to False so that the loop continues to run

cmd_args = sys.argv[1:]
league = None
if len(cmd_args) >= 1:
    league = "\t\t\t\t\t" + cmd_args[0]
else:
    league = "\t\t\t\t\tEURO 2020 Group D"
print("=============================================================")  # prints '=' repeatedly
print(league)                                    # prints message
print("=============================================================")  # prints '=' repeatedly
l = ""                                                                  # creating a null string variable
print(f"Teams{l:14}P{l:4}W{l:4}D{l:4}L{l:4}F{l:4}A{l:4}Diff{l:4}Pts{l:4}")  # prints message
for x in l_objects:                                                     # for loop goes through the l_objects list
    x.display()                                                         # calls the display function from the Team class



