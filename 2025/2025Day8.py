import math
import re

gd = [
"162,817,812",
"57,618,57",
"906,360,560",
"592,479,940",
"352,342,300",
"466,668,158",
"542,29,236",
"431,825,988",
"739,650,466",
"52,470,668",
"216,146,977",
"819,987,18",
"117,168,530",
"805,96,715",
"346,949,466",
"970,615,88",
"941,993,340",
"862,61,35",
"984,92,344",
"425,690,689"
]

#f = open("2025\\2025Day8.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

coords = []
for g in game_data:
    coord = g.split(',')
    coords.append( ( int(coord[0]), int(coord[1]), int(coord[2]) ) )

# create a list wiht all possible 
pairs = []
for i in range(0,len(coords)):
    c1 = coords[i]
    for c2 in coords[i+1:]:
        pairs.append( (c1 , c2) ) 

# sort list
def myFunc(e):
  c1 = e[0]
  c2 = e[1]
  return math.sqrt((abs(c1[0] - c2[0])**2) + (abs(c1[1] - c2[1])**2) + (abs(c1[2] - c2[2])**2))

pairs.sort(key=myFunc)

# build circuits
circuits = { }
num = 1
for i in range(0,10):
   print(i+1)
   print(pairs[i])
   p1 = pairs[i][0]
   p2 = pairs[i][1]
   join = False
   for k, c in circuits.items():
      for cs in c:
         if (cs == p1 or cs == p2):
            join = True
            break
      if join:
         break
   if join:
      ns = circuits.get(k)
      ns.add(p1)
      ns.add(p2)
      circuits.update( {k : ns })           
   else:
      circuits[num] = { p1, p2 }
      num += 1

print(circuits)

l = []
for k, c in circuits.items():
   l.append((len(c)))

l.sort(reverse=True)
print(l)

total = 1
for i in range(0,3):
   total *= l[i]
print("Total is " + str(total))

# 6480 is too low
'''
pairs = {}
for i in range(0,len(coords)):
    c1 = coords[i]
    for c2 in coords[i+1:]:
        dist = math.sqrt((abs(c1[0] - c2[0])**2) + (abs(c1[1] - c2[1])**2) + (abs(c1[2] - c2[2])**2))
        pairs[ ( c1 , c2 ) ] = dist
print(pairs)

closest = 9999
for k,v in pairs.items():
    if v < closest:
        print("Closest " + str(v) + " pair " + str(k))
        p = k
        closest = v
print(p)
'''