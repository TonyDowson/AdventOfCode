import math
import re

gd = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."
]

f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day4.txt", "r")
gd = f.readlines()

def checkmap(coord,map):
   if coord in map:
      return 1
   else:
      return 0

game_data = [i.strip('\n') for i in gd]

map = {}
x = 0
y = 0
for i in game_data:
   x = 0
   for j in i:
      if j == '@':
         map[(x,y)] = j
      x += 1
   y += 1

print(map)

total = 0
for i in map.keys():
   sub = 0
   sub += checkmap((i[0]-1,i[1]-1),map)
   sub += checkmap((i[0],i[1]-1),map)   
   sub += checkmap((i[0]+1,i[1]-1),map)      

   sub += checkmap((i[0]-1,i[1]),map)
   sub += checkmap((i[0]+1,i[1]),map)   

   sub += checkmap((i[0]-1,i[1]+1),map)
   sub += checkmap((i[0],i[1]+1),map)   
   sub += checkmap((i[0]+1,i[1]+1),map)      

   print("Checking..." + str(i) + " adjacent=" + str(sub))
   if sub < 4:
      total += 1

print("Total part 1 " + str(total))


total = 0
for i in range(0,100):
   paper = []
   for i in map.keys():
      sub = 0
      sub += checkmap((i[0]-1,i[1]-1),map)
      sub += checkmap((i[0],i[1]-1),map)   
      sub += checkmap((i[0]+1,i[1]-1),map)      

      sub += checkmap((i[0]-1,i[1]),map)
      sub += checkmap((i[0]+1,i[1]),map)   

      sub += checkmap((i[0]-1,i[1]+1),map)
      sub += checkmap((i[0],i[1]+1),map)   
      sub += checkmap((i[0]+1,i[1]+1),map)      

      #print("Checking..." + str(i) + " adjacent=" + str(sub))
      if sub < 4:
         total += 1
         paper.append(i)

   print(paper)
   if paper == []:
      print("No more")
      break

   for p in paper:
      map.pop(p)

print("Total part 2 " + str(total))
