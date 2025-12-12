import math
import re

gd = [
   "7,1",
   "11,1",
   "11,7",
   "9,7",
   "9,5",
   "2,5",
   "2,3",
   "7,3"
]

f = open("2025\\2025Day9.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

coords = []
for g in game_data:
    coord = g.split(',')
    coords.append( ( int(coord[0]), int(coord[1]) ) )

# create a list with all possible 
pairs = []
for i in range(0,len(coords)):
    c1 = coords[i]
    for c2 in coords[i+1:]:
        pairs.append( (c1 , c2) ) 

# sort list
def myFunc(e):
  c1 = e[0]
  c2 = e[1]
  #return (math.sqrt((abs(c1[0] - c2[0])**2) + (abs(c1[1] - c2[1])**2)))
  return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)  

pairs.sort(reverse=True,key=myFunc)

for j in pairs[0:10]:
   c1 = j[0]
   c2 = j[1]   
   area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)     
   print(str(j) + " value = " + str(myFunc(j)) + " Area = " + str(area))

maxarea = 0
for j in pairs:
   c1 = j[0]
   c2 = j[1]
   area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)    
   if area > maxarea:
      maxarea = area
print("Total= "+ str(maxarea))

c1 = pairs[0][0]
c2 = pairs[0][1]
area = (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)  
print("Total= "+ str(area))
# 4347478493 - Answer is too low