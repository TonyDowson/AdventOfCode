def getletters(grid,coords,letters,vertical,horizontal):
   word = grid[coords]
   try:
      word += grid[(coords[0]+horizontal,coords[1]+vertical)]
      word += grid[(coords[0]+horizontal*2,coords[1]+vertical*2)]
      if letters > 2:
         word += grid[(coords[0]+horizontal*3,coords[1]+vertical*3)]
   except KeyError:
      word = "VOID"
   return word

def find_xmas(grid,coords):
   xmascount = 0
   if getletters(grid,coords,3,0,1) == 'XMAS':
      xmascount += 1
   if getletters(grid,coords,3,0,-1) == 'XMAS':
      xmascount += 1      
   if getletters(grid,coords,3,1,0) == 'XMAS':
      xmascount += 1
   if getletters(grid,coords,3,-1,0) == 'XMAS':
      xmascount += 1

   if getletters(grid,coords,3,1,1) == 'XMAS':
      xmascount += 1
   if getletters(grid,coords,3,-1,1) == 'XMAS':
      xmascount += 1
   if getletters(grid,coords,3,1,-1) == 'XMAS':
      xmascount += 1      
   if getletters(grid,coords,3,-1,-1) == 'XMAS':
      xmascount += 1    

   return xmascount

def find_mas(grid,coords):
   a = []
   if getletters(grid,coords,2,1,1) == 'MAS':
      a.append((coords[0] + 1, coords[1] + 1))
   if getletters(grid,coords,2,-1,1) == 'MAS':
      a.append((coords[0] + 1, coords[1] - 1))      
   if getletters(grid,coords,2,1,-1) == 'MAS':
      a.append((coords[0] - 1, coords[1] + 1))      
   if getletters(grid,coords,2,-1,-1) == 'MAS':
      a.append((coords[0] - 1, coords[1] - 1))

   return a

gd = [
   "MMMSXXMASM\n",
   "MSAMXMSMSA\n",
   "AMXSXMAAMM\n",
   "MSAMASMSMX\n",
   "XMASAMXAMM\n",
   "XXAMMXXAMA\n",
   "SMSMSASXSS\n",
   "SAXAMASAAA\n",
   "MAMMMXMMMM\n",
   "MXMXAXMASX\n"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024Day4.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Build word grid
y = 0
wordgrid = {}
for g in game_data:
   for i in range(len(g)):
      wordgrid[(i,y)] = g[i]
   y += 1   

# Part 1
total = 0
for i in wordgrid.items():
   if i[1] == 'X':         
      total += find_xmas(wordgrid,i[0])
print("Part 1 " + str(total))

# Part 2
listofas  = []
for i in wordgrid.items():
   if i[1] == 'M':         
      listofas += find_mas(wordgrid,i[0])

setofas = set(listofas)
total = len (listofas) - len(setofas)
      
print("Part 2 " + str(total))
