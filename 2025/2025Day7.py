import math
import re

gd = [
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"..............."
]

f = open("2025\\2025Day7.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# map the board
y = 0
map = {}
for i in game_data:
   for j in range(0,len(i)):
      c = i[j]
      if c == '^':
         map[(j,y)] = c
      if c == 'S':
         startx = j
   y += 1

maxy = y
print(map)

# part 1 - dictionary
beams = { (startx,1): '!' }
num_of_splits = 0
for y in range(1,maxy):
   newbeams = {}
   for b in beams:
      if (b[0],y) in map:
         newbeams[ (b[0]-1,y) ] = '!'
         newbeams[ (b[0]+1,y) ] = '!'  
         num_of_splits += 1
      else:
         newbeams[(b[0],y)] = '!'
   beams = newbeams             

print(beams)
print("Total using a dictionary= " +str(num_of_splits))

# part 1 - set
beams = { (startx,1) }
num_of_splits = 0
for y in range(1,maxy):
   newbeams = set()
   for b in beams:
      if (b[0],y) in map:
         newbeams.add((b[0]-1,y))
         newbeams.add((b[0]+1,y))
         num_of_splits += 1
      else:
         newbeams.add((b[0],y))
   beams = newbeams             

print("Total using a set= " +str(num_of_splits))

# part 2 - dictionary
beams = { (startx,1): 1 }
for y in range(1,maxy):
   newbeams = {}
   for b,v in beams.items():
      if (b[0],y) in map:               
         newbeams.update({(b[0]-1,y): newbeams.get((b[0]-1,y), 0)+v})            
         newbeams.update({(b[0]+1,y): newbeams.get((b[0]+1,y), 0)+v})                     
      else:
         newbeams.update({(b[0],y): newbeams.get((b[0],y), 0)+v})              
   beams = newbeams
              
print(beams)
total = 0
for i in beams.values():
   total += i
print("Part 2 Total= " + str(total))

'''
# part 2 - takes too long building a list
beams = [ (startx,1) ]
num_of_splits = 0
for y in range(1,maxy):
   newbeams = []
   beams.sort()
   print(str(beams) + " " + str(len(beams)))
   for b in beams:
      if (b[0],y) in map:
         newbeams.append( (b[0]-1,y) )
         newbeams.append( (b[0]+1,y) )
         num_of_splits += 1 
      else:
         newbeams.append( (b[0],y) )
   beams = newbeams

print(beams)
print("Total= " +str(len(beams)))

'''