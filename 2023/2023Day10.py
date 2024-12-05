def BuildMap(game_data):
    row=0
    dotcount = 0
    map = []
    for x in game_data:
        print(x)
        col = 0
        for y in x:
            if (y != '\n'):
                map.append((y, (row,col)))
                if (y == '.'):
                    dotcount += 1
            col += 1
        row += 1
    print("DotCount="+str(dotcount))
    return map

def traverseMap(map):
    step = 0
    # find starting position
    for m in map:
        if (m[0] == "S"):
            pos = m

    print("Starting pos " + str(pos))
    prevpos = ('S', (0,0))
    end = False
    prevstep = step
    while (not end):
        coords = []
        for m in map:
            if ((abs(m[1][0] - pos[1][0]) == 1 and abs(m[1][1] - pos[1][1]) == 0) or
                (abs(m[1][0] - pos[1][0]) == 0 and abs(m[1][1] - pos[1][1]) == 1)):
                if (not (prevpos[1][0] == m[1][0] and prevpos[1][1] == m[1][1])):
                    coords.append(m)
                    if (len(coords) == 3):
                        break

        
        prevpos = pos
       #if (step == 0):
       #     coords.sort() 
        #print("prevpos " + str(prevpos))
        print("coords (row,col)="+str(coords) + " m=" + str(pos))
        for m in coords:
            # Take first symbol which is valid for pos
            # Veritical pipe is valid in 2 positions - above or below pos
            # | is a vertical pipe connecting north and south.
            if (m[0] == "|" and
                ((m[1][0]+1 == pos[1][0] and pos[0] in ['S','|','L','J']) or
                 (m[1][0]-1 == pos[1][0] and pos[0] in ['S','|','F','7']))):   
                pos = m
                step += 1 
                print("Moved | " + str(pos))
                break
            # - is a horizontal pipe connecting east and west.
            elif (m[0] == "-" and 
                ((m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','J','7']) or
                 (m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','F','L']))):                
                pos = m
                step += 1 
                print("Moved - " + str(pos))
                break
            #L is a 90-degree bend connecting north and east.            
            elif (m[0] == "L" and 
                ((m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','F','7']) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','7','J']))):
                pos = m
                step += 1 
                print("Moved L " + str(pos))
                break
            #7 is a 90-degree bend connecting south and west.            
            elif (m[0] == "7" and 
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','J','L']) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','L','F']))):
                pos = m
                step += 1 
                print("Moved 7 " + str(pos)) 
                break
            #J is a 90-degree bend connecting north and west.
            elif (m[0] == "J" and 
                ((m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','F','7']) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','F','L']))):
                pos = m
                step += 1 
                print("Moved J " + str(pos)) 
                break            
            #F is a 90-degree bend connecting south and east.      
            elif (m[0] == "F" and 
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','L','J'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','7','J'] ))):
                pos = m
                step += 1 
                print("Moved F " + str(pos)) 
                break  
            elif (m[0] == "S" and
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['|','L','J'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['-','7','J'] ) or
                 (m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['|','F','7'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['-','F','L'] )) ):                                 
                pos = m
                step += 1 
                print("Moved S " + str(pos)) 
                end = True
                break 

            #print("Not Moved step=" + str(step) + " pos=" + str(pos) + " m=" + str(m)) 
        if (step == prevstep):
            end = True
        else:
            prevstep = step
    return step

game_data = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ..."
]

game_data2 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day10.txt", "r")
game_data = f.readlines()

map = BuildMap(game_data)
print("Total "+ str(traverseMap(map)/2))