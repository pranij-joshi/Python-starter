# defining a class Team
class Team:
    # init function for class Team
    def __init__(self):
        self.teams = {}                                         # declaring an empty dictionary for the class
        self.l = []                                              # declaring an empty list for the class


    # function to read file and store in the list self.l
    def readfile_games(self):
        f = open("rugby.csv", "r")                              # opening the file
        line = f.readlines()                                     # reads the line in the file one line at a time
        for x in line:
            y = x.strip()
            self.l.append(y.split(","))
        f.close()                                               # closes the file


    # to store the team score
    def teams_score(self):
        temp = set()
        for i in self.l:                # loop runs in the given range
            temp.add(i[0])
            temp.add(i[2])
        temp = list(temp)
        for x in temp:
            self.teams[x] = {"P": 0, "W": 0, "D": 0, "L": 0, "F": 0, "A": 0, "Diff": 0, "Pts": 0}       # intializing the dictionary

        for x in self.l:                # loop runs in the given range
            self.teams[x[0]]["P"] += 1                 # increments the played games for first team by 1
            self.teams[x[2]]["P"] += 1             # increments the played games for second team by 1

            if int(x[1]) > int(x[3]):                   # if the first team goals is greater
                self.teams[x[0]]["W"] += 1             # increments the win by 1 for the first team
                self.teams[x[2]]["L"] += 1         # increments the loss by 1 for the second team
                self.teams[x[0]]["Pts"] += 3           # increases the points for the winning team by 1
                self.teams[x[0]]["F"] += int(x[1])        # increases the goal scored by the first team
                self.teams[x[2]]["F"] += int(x[3])    # increases the goal scored by the second team
                self.teams[x[0]]["A"] += int(x[3])
                self.teams[x[2]]["A"] += int(x[1])

            elif int(x[1]) < int(x[3]):
                self.teams[x[2]]["W"] += 1
                self.teams[x[0]]["L"] += 1
                self.teams[x[2]]["Pts"] += 3
                self.teams[x[2]]["F"] += int(x[3])
                self.teams[x[0]]["F"] += int(x[1])
                self.teams[x[2]]["A"] += int(x[1])
                self.teams[x[0]]["A"] += int(x[3])
            else:
                self.teams[x[0]]["D"] += 1
                self.teams[x[2]]["D"] += 1
                self.teams[x[0]]["Pts"] += 1
                self.teams[x[2]]["Pts"] += 1
                self.teams[x[2]]["F"] += int(x[3])
                self.teams[x[0]]["F"] += int(x[1])
                self.teams[x[2]]["A"] += int(x[1])
                self.teams[x[0]]["A"] += int(x[3])

        for k in self.teams.keys():
            self.teams[k]["Diff"] = self.teams[k]["F"] - self.teams[k]["A"]

    def sort_display(self):
        sorted_teams = sorted(self.teams.items(), key=lambda x:x[1]["Pts"], reverse=True)
        breaker = False
        while breaker == False:
            breaker = True
            for x in range(0, len(sorted_teams)-1):
                if sorted_teams[x][1]['Pts'] == sorted_teams[x+1][1]['Pts']:
                    if sorted_teams[x][1]['Diff'] < sorted_teams[x+1][1]['Diff']:
                        temp = sorted_teams[x+1]
                        sorted_teams[x+1] =sorted_teams[x]
                        sorted_teams[x] = temp
                        breaker = False
                    elif sorted_teams[x][1]['Diff'] == sorted_teams[x+1][1]['Diff']:
                        if sorted_teams[x][1]['F'] < sorted_teams[x + 1][1]['F']:
                            temp = sorted_teams[x + 1]
                            sorted_teams[x + 1] = sorted_teams[x]
                            sorted_teams[x] = temp
                            breaker = False



        print("=============================================================")
        print("\t\t\t\t\tEURO 2020 Group D")
        print("=============================================================")
        l = ""
        print(f"Teams{l:15}P{l:4}W{l:4}D{l:4}L{l:4}F{l:4}A{l:4}Diff{l:4}Pts{l:4}")
        for x in range(0, len(sorted_teams)):
            print(f"{sorted_teams[x][0]:15}{sorted_teams[x][1]['P']:6}{sorted_teams[x][1]['W']:5}{sorted_teams[x][1]['D']:5}"
                  f"{sorted_teams[x][1]['L']:5}{sorted_teams[x][1]['F']:5}{sorted_teams[x][1]['A']:5}{sorted_teams[x][1]['Diff']:6}"
                  f"{sorted_teams[x][1]['Pts']:8}")


s = Team()                  #creating an instance of Team class
s.readfile_games()          #calling function readfile_games() of Team class
s.teams_score()             #calling function teams_score() of Team class
s.sort_display()            #calling function sort_display() of Team class