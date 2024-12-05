from datetime import datetime
from math import lcm

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day8.txt", "r")
#print(datetime.now())
pattern = f.readline().replace("\n","")
f.readline()
maps = {}
pos = []

for x in f:
    v = x.replace("\n","").split()
    maps[v[0]] = ( v[2].strip(",()"), v[3].strip(",()") ) 
    if (v[0].endswith("A")):
        pos.append(v[0])

print(pattern)
print(maps)
print(pos)

results = []
for p in pos:
    steps = 0     
    newpos = p 
    while (not newpos.endswith("Z")):
        for x in pattern:
            if (x == "R"):
                newpos = maps[newpos][1]
            if (x == "L"):
                newpos = maps[newpos][0]
            steps = steps + 1
            if (newpos.endswith("Z")):
                break           

    print("start=" + str(p) + " end=" + newpos  + " steps=" + str(steps)) 
    results.append(steps)
      
print(results)
total = lcm(results[0], results[1], results[2], results[3], results[4], results[5])

print ("Answer is " + str(total))
#print(datetime.now())