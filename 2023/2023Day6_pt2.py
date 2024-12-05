
from datetime import datetime

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day6.txt", "r")
total = 1

print(datetime.now())

time = f.readline().replace(" ","").replace("\n","").split(":")
dist = f.readline().replace(" ","").split(":")

print(time)
print(dist)

for i in range(1,len(time)):
    t = int(time[i])
    wins = 0
    
    for j in range(1,t):
        res = (t - j) * j
        #print("res="+str(res) + " Dist to Beat="+str(dist[i]))

        if (res > int(dist[i])):
            wins = wins + 1

    print("Wins="+str(wins))
    total = total * wins

print ("Answer is")
print(total)
print(datetime.now())