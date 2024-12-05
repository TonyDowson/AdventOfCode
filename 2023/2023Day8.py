from datetime import datetime

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day8.txt", "r")
print(datetime.now())

# Read pattern and skip line in between
pattern = f.readline().strip("\n")
f.readline()

maps = {}
for x in f:
    v = x.strip("\n").split()
    maps[v[0]] = ( v[2].strip(",()"), v[3].strip(",()") ) 

print(pattern)
print(maps)

pos = 'AAA'
steps = 0
while (pos != "ZZZ"):
    for x in pattern:
        if (pos != "ZZZ"):
            steps = steps + 1            
            if (x == "R"):
                pos = maps[pos][1]
            if (x == "L"):
                pos = maps[pos][0]
        else:
            break

print ("Answer is " + str(steps))
print(datetime.now())