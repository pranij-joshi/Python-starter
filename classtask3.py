
f = open("games.txt", "r")
line = f.readline()
temp = ""
l=[]
matches = {}
while line != "":

    for letter in line:
        if letter == "," or letter == "\n":
            l.append(temp)
            temp = ""

        else:
            temp = temp + letter
    line = f.readline()
l.append(temp) #edit this in loop
print(l)
#print(l)
count = 0

for i in range(0, int(len(l)/2)):
    matches[l[count]] = {"P":0, "W":0, "D":0, "L":0, "F":0, "A":0, "Diff":0, "Pts":0}
    count += 2


count = 0
for x in range(0, int(len(l)/4)):
    matches[l[count]]["P"] += 1
    matches[l[count+2]]["P"] += 1


    if l[count + 1] > l[count +3]:
        matches[l[count]]["W"] += 1
        matches[l[count+2]]["L"] += 1
        matches[l[count]]["Pts"] += 3
        matches[l[count]]["F"] += int(l[count+1])
        matches[l[count + 2]]["F"] += int(l[count+3])
        matches[l[count]]["A"] += int(l[count+3])
        matches[l[count + 2]]["A"] += int(l[count+1])

    elif l[count + 1] < l[count +3]:
        matches[l[count+2]]["W"] +=1
        matches[l[count]]["L"] += 1
        matches[l[count+2]]["Pts"] += 3
        matches[l[count+2]]["F"] += int(l[count+3])
        matches[l[count]]["F"] += int(l[count+1])
        matches[l[count + 2]]["A"] += int(l[count + 1])
        matches[l[count]]["A"] += int(l[count + 3])
    else:
        matches[l[count]]["D"] += 1
        matches[l[count+2]]["D"] += 1
        matches[l[count]]["Pts"] += 1
        matches[l[count+2]]["Pts"] += 1
        matches[l[count + 2]]["F"] += int(l[count + 3])
        matches[l[count]]["F"] += int(l[count + 1])
        matches[l[count + 2]]["A"] += int(l[count + 1])
        matches[l[count]]["A"] += int(l[count + 3])
    count += 4


for k in matches.keys():
    matches[k]["Diff"] = matches[k]["F"] - matches[k]["A"]

matches_sorted = sorted(matches.items(), key=lambda x:x[1]["Pts"], reverse=True)
print(matches_sorted)
print(matches)
