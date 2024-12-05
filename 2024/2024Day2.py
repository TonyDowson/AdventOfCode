def isitsafe(vals):
   diffs = []
   for i in range(1,len(vals)):
      diffs.append(int(vals[i-1]) - int(vals[i]))

   safe = True
   firstnum = diffs[0]

   for i in diffs:
      if i < -3 or i > 3 or i == 0:
         safe = False
      if (firstnum > 0 and i < 0):
            safe = False
      elif (firstnum < 0 and i > 0):        
           safe = False
      
   return safe

gd = [
"7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9",
"9 10 9 11 14 16 17 20"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024Day2.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Part 1
safe = 0
for i in game_data:
   vals = i.split()
   if isitsafe(vals):
      safe += 1

print("Part 1 = " + str(safe))

# Part 2
safe = 0
for i in game_data:
   vals = i.split()
   for i in range(len(vals)):
      l = vals.copy()
      del l[i]
      if isitsafe(l):
         safe += 1
         break

print("Part 2 = " + str(safe))
# 624 is too low