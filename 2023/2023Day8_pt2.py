from datetime import datetime
import re

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day8.txt", "r")
total = 0

pattern = f.readline().replace("\n","")
maps = {}
pos = []
f.readline()

for x in f:
    v = x.replace("\n","").split()
    maps[v[0]] = ( v[2].strip(",()"), v[3].strip(",()") ) 
    if (v[0].endswith("A")):
        pos.append(v[0])

print(pattern)
print(maps)

steps = 0
while True:
    for x in pattern:
        newpos = []
        if ((steps % 10000000) == 0):
            print("step="+str(steps))
            #print("pos=" +str(pos))            

        for p in pos:
            if (x == "R"):
                newpos.append(maps[p][1])
            if (x == "L"):
                newpos.append(maps[p][0])

        steps = steps + 1
        pos = newpos 

        allZ = True
        Zs = 0
        for p in newpos:
            if (not p.endswith("Z")):
                allZ = False
            else:
                Zs=Zs+1
        
        if (Zs > 3):
            print("Nearly "+str(Zs))
            print(newpos)

        if (allZ):
            break                

    if (allZ):
        break           



print ("Answer is")
print(steps)
print(datetime.now())