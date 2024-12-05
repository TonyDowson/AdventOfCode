def BuildMap(game_data, empty_cols):
    row=0
    map = []
    for x in game_data:
        print(x)
        col = 0
        for y in x:
            if (y != '\n'):
                map.append((y, (row,col)))
            if (col in empty_cols):
                col += 999999
            col += 1

        if (all(element == '.' for element in x)):
            row += 999999
        row += 1
    return map

def findEmptyCols(game_data):
    cols = []
    colnum = 0

    for c in range(len(game_data)):
        allDot = True

        for r in range(len(game_data[0])):
            if (game_data[r][c] == '#'):
                allDot = False
        
        if (allDot):
            print("col=" + str(c) + " is empty")
            cols.append(c + (len(cols)*999999))
                
    return cols

def getDist(map):
    galaxies = []
    dist = 0    

    for i in map:
        if (i[0] == '#'):
           galaxies.append(i[1])
    print(galaxies)

    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            d = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            #print("From " + str(i+1) + " " + str(galaxies[i]) + " To " + str(j+1) + " " + str(galaxies[j]) + " dist=" + str(d))
            dist += d

    return dist

gd = [
    "...#......\n",
    ".......#..\n",
    "#.........\n",
    "..........\n",
    "......#...\n",
    ".#........\n",
    ".........#\n",
    "..........\n",
    ".......#..\n",
    "#...#.....\n"
]




f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day11.txt", "r")
gd = f.readlines()

game_data = []
for i in gd:
    game_data.append(i.rstrip('\n'))

empty_cols = findEmptyCols(game_data)
print(empty_cols)
map = BuildMap(game_data, empty_cols)
print(map)

print("Total "+ str(getDist(map)))