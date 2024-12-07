def traverse_map(map, pos):
   loop = 0
   visited = set()
   dir = (0,-1)

   while True:
      try:
         #print("Pos=" + str(pos) + " Dir=" + str(dir))
         newpos = (pos[0] + dir[0], pos[1] + dir[1])
         
         if map[newpos] == 'O' and loop < 2:
            loop += 1       
         elif (loop == 3 and map[newpos] == 'O'):            
            print("Loop")
            visited = set()
            break

         if map[newpos] == '#' or map[newpos] == 'O':
            # change direction
            if dir[0] == 0 and dir[1] == -1:
               dir = (1,0)
            elif dir[0] == 1 and dir[1] == 0:
               dir = (0,1)  
            elif dir[0] == 0 and dir[1] == 1:
               dir = (-1,0)
            else: 
               dir = (0,-1)
         else:
            visited.add(newpos)
            pos = newpos

      except KeyError:
         print("Key Error " +  str(newpos))
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

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024\\2024Day6.txt", "r")
#gd = f.readlines()

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

print(pos)
print("Total for Part 1 " + str(traverse_map(map, pos)))

loop = 0
for i in map.keys():
   print(i)

   v = map[i]
   if v == '#' or v == '^':
      print("Skip")
      continue
   map[i] = 'O'

   if traverse_map(map,pos) == 0:
      loop += 1
   map[i] = v


print("Total for Part 2 " + str(loop))