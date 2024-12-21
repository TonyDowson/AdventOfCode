def traverse_map(map, pos):
   loop = 0
   visited = set()
   dir = (0,-1)

   while True:
      try:
         #print("Pos=" + str(pos) + " Dir=" + str(dir))
         newpos = (pos[0] + dir[0], pos[1] + dir[1])

         if map[newpos] == '#' or map[newpos] == 'O':
            # change direction
            #print("Will Hit="+ str(map[newpos]) + " Pos=" + str(pos) + " Dir=" + str(dir) + " Visited=" + str(len(visited)))
            if dir[0] == 0 and dir[1] == -1:
               dir = (1,0)
            elif dir[0] == 1 and dir[1] == 0:
               dir = (0,1)  
            elif dir[0] == 0 and dir[1] == 1:
               dir = (-1,0)
            else: 
               dir = (0,-1)
         else:
            previouslen = len(visited)
            visited.add(newpos)
            pos = newpos
            if (len(visited) == previouslen):
               loop += 1
               # This is brute brute force !! Very inefficient but does work
               if loop > 200:
                  #print("Loop")
                  visited = set()
                  break
            else:
               loop = 0

      except KeyError:
         #print("Key Error " +  str(newpos))
         break

   return len(visited)

gd = [
   "....#.....\n",
   ".........#\n",
   "..........\n",
   "..#.......\n",
   ".......#..\n",
   "..........\n",
   ".#..^.....\n",
   "........#.\n",
   "#.........\n",
   "......#..."
]

f = open("2024\\2024Day6.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Build word grid
y = 0
map = {}
for g in game_data:
   for i in range(len(g)):
      if g[i] == '#' or g[i] == '.':
         map[(i,y)] = g[i]
      elif g[i] == '^':
         map[(i,y)] = g[i]
         pos = (i,y)
   y += 1   
print("Total for Part 1 " + str(traverse_map(map, pos)))

loop = 0
for i in map.keys():
   #print(i)

   v = map[i]
   if v == '#' or v == '^':
      #print("Skip")
      continue
   map[i] = 'O'

   if traverse_map(map,pos) == 0:
      loop += 1
   map[i] = v


print("Total for Part 2 " + str(loop))