

def mapLayout(layout):
    map = {}
    row, col = 0,0
    print(layout)
    for l in layout:
        for v in l:
            map[(row, col)] = v
            col +=1
        col = 0
        row += 1
    return map, row, col

def validRowCol(row,col):
    #print("row=" + str(row) + " col="+str(col))
    if (row < 0 or col < 0):
        return False
    elif (row > 109 or col > 109):
        return False
    
    return True
    
def move(row,col,dir):
    if dir == 'N':
        row -= 1
    elif dir == 'S':
        row += 1
    elif dir == 'W':
        col -= 1
    elif dir == "E":
        col += 1
    else:
        AssertionError

    return row, col

# dir is N W E S
def traverseMap(map,beento,row,col,dir):
    energised = []
    while validRowCol(row,col):
        #print(energised)   
        
        energised.append( (row,col) )   
        if ((row, col, dir) in beento):
            #print("BEEN HERE BEFORE")
            break
        else:
            beento.append( (row, col, dir) )   
        #print("Visited " + str(beento))

        letter = map[ (row, col)]        
        #print(str(row) + " " + str(col) + " " +letter+" "+dir)             
        if letter == '|' and dir in ['W','E']:
            dir = 'S'
            # and it splits 
            #print("Split on |")            
            energised += traverseMap(map,beento,row,col,'N')
            #print("Split on | - COMPLETE")              
        elif letter == '-' and dir in ['N','S']:
            dir = 'W'
            # and it splits 
            #print("Split on -")
            energised += traverseMap(map,beento,row,col,'E')
        elif letter == '/':
            if dir == 'N':
                dir = 'E'
            elif dir == 'E':
                dir = 'N'
            elif dir == 'S':
                dir = 'W'        
            elif dir == 'W':
                dir = 'S'       
        elif letter == "B":
            if dir == 'N':
                dir = 'W'
            elif dir == 'W':
                dir = 'N'
            elif dir == 'S':
                dir = 'E'        
            elif dir == 'E':
                dir = 'S'                                           

        row, col = move(row,col,dir)
    
    return energised


game_data = [
    ".|...\....\n",
    "|.-.\.....\n",
    ".....|-...\n",
    "........|.\n",
    "..........\n",
    ".........\\n",
    "..../.\\..\n",
    ".-.-/..|..\n",
    ".|....-|.\\n",
    "..//.|....\n"
]

game_data = [
".|...B....\n",
"|.-.B.....\n",
".....|-...\n",
"........|.\n",
"..........\n",
".........B\n",
"..../.BB..\n",
".-.-/..|..\n",
".|....-|.B\n",
"..//.|....\n"
]

f = open("2023Day16.txt", "r")
game_data = f.readlines()

map, maxrow, maxcol = mapLayout([g.rstrip('\n') for g in game_data])
print(map)
total = 0
max = 0

for i in range(110):
	energised = traverseMap(map, [] ,0,i,'S')
	total = len(list(dict.fromkeys(energised)))
	print(str(i) + '=' + str(total))
	if total > max:
		max = total
		
for i in range(110):
	energised = traverseMap(map, [] ,109,i,'N')
	total = len(list(dict.fromkeys(energised)))
	print(str(i) + '=' + str(total))
	if total > max:
		max = total
		
for i in range(110):
	energised = traverseMap(map, [] ,0,i,'E')
	total = len(list(dict.fromkeys(energised)))
	print(str(i) + '=' + str(total))
	if total > max:
		max = total
		
for i in range(110):
	energised = traverseMap(map, [] ,109,i,'W')
	total = len(list(dict.fromkeys(energised)))
	print(str(i) + '=' + str(total))
	if total > max:
		max = total
		
print(total)
