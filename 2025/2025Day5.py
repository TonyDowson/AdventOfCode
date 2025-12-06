import math
import re

gd = [
"3-5",
"10-14",
"16-20",
"14-16",
"12-18",
"",
"1",
"5",
"8",
"11",
"17",
"32"
]

gd = [
   "1-10",
   "5-15",
   "8-12",
   "",
   "1"
]


f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day5.txt", "r")
gd = f.readlines()

def checkmap(coord,map):
   if coord in map:
      return 1
   else:
      return 0

game_data = [i.strip('\n') for i in gd]
ranges = []
vals = []
nextset = False


for i in game_data:
   if i == '':
      nextset = True
      continue

   if not nextset:
      v = i.split('-')
      ranges.append( (int(v[0]),int(v[1])) )

   if nextset:
      vals.append(int(i))

print(ranges)
print(vals)

total = 0
for i in vals:
   for j in ranges:
      if i >= j[0] and i <= j[1]:
         total += 1
         break

print("Total part 1 " + str(total))


ranges.sort()
total = 0
done = []

for i in range(0,len(ranges)):
   if ranges[i] in done:
      continue

   start = ranges[i][0]
   end = ranges[i][1]

   for j in range(i+1,len(ranges)):
      print(ranges[j])
      print("Start=" + str(start) + " End=" + str(end))      
      if start <= ranges[j][0] and end >= ranges[j][1]:
         # complete overlap and so ignore
         done.append(ranges[j])
         continue    
      if end >= ranges[j][0]:
         # overlap
         done.append(ranges[j])         
         end = ranges[j][1]
         continue

   total += (end+1 - start)


# 384228184818274 is too high
# 357193158632481 is too high
# 352807801032185 is too high
# 352807801032181 not right
# 352807801032167 correct !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print("Total part 2 " + str(total))