from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def calculateDot(polygon, map):
    dotcount = 0
    print(polygon)
    polygon = Polygon(polygon)    
    for d in map:
        point = Point(d[1][0], d[1][1])
        if (polygon.contains(point)):
            dotcount+= 1

    return dotcount    


def BuildMap(game_data):
    row=0
    map = []
    for x in game_data:
        print(x)
        col = 0
        for y in x:        
            if (y != '\n'):
                map.append((y, (row,col)))
            col += 1
        row += 1
    return map

def traverseMap(map):
    step = 0
    prevpos = ('S', (0,0))
    end = False
    polygon = []

    # find starting position
    for m in map:
        if (m[0] == "S"):
            pos = m

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
        #print("coords (row,col)="+str(coords) + " m=" + str(pos))

        for m in coords:
            # Take first symbol which is valid for pos
            # Veritical pipe is valid in 2 positions - above or below pos
            # | is a vertical pipe connecting north and south.
            if (m[0] == "|" and
                ((m[1][0]+1 == pos[1][0] and pos[0] in ['S','|','L','J']) or
                 (m[1][0]-1 == pos[1][0] and pos[0] in ['S','|','F','7']))):   
                pos = m
                polygon.append(m[1])
                step += 1 
                #print("Moved | " + str(pos))
                break
            # - is a horizontal pipe connecting east and west.
            elif (m[0] == "-" and 
                ((m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','J','7']) or
                 (m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','F','L']))):                
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved - " + str(pos))
                break
            #L is a 90-degree bend connecting north and east.            
            elif (m[0] == "L" and 
                ((m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','F','7']) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','7','J']))):
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved L " + str(pos))
                break
            #7 is a 90-degree bend connecting south and west.            
            elif (m[0] == "7" and 
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','J','L']) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','L','F']))):
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved 7 " + str(pos)) 
                break
            #J is a 90-degree bend connecting north and west.
            elif (m[0] == "J" and 
                ((m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','F','7']) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['S','-','F','L']))):
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved J " + str(pos)) 
                break            
            #F is a 90-degree bend connecting south and east.      
            elif (m[0] == "F" and 
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['S','|','L','J'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['S','-','7','J'] ))):
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved F " + str(pos)) 
                break  
            elif (m[0] == "S" and
                ((m[1][0]+1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['|','L','J'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]+1 == pos[1][1] and pos[0] in ['-','7','J'] ) or
                 (m[1][0]-1 == pos[1][0] and m[1][1] == pos[1][1] and pos[0] in ['|','F','7'] ) or
                 (m[1][0] == pos[1][0] and m[1][1]-1 == pos[1][1] and pos[0] in ['-','F','L'] )) ):    
                pos = m
                polygon.append(m[1])                
                step += 1 
                #print("Moved S " + str(pos)) 
                end = True
                break 

    return step, polygon

game_data1 = [
    ".....",
    ".S-7.",
    ".|.|.",
    ".L-J.",
    "....."
]

game_data2 = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ..."
]

game_data3 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "..........."
]

game_data4 = [
    ".F----7F7F7F7F-7....",
    ".|F--7||||||||FJ....",
    ".||.FJ||||||||L7....",
    "FJL7L7LJLJ||LJ.L-7..",
    "L--J.L7...LJS7F-7L7.",
    "....F-J..F7FJ|L7L7L7",
    "....L7.F7||L7|.L7L7|",
    ".....|FJLJ|FJ|F7|.LJ",
    "....FJL-7.||.||||...",
    "....L---J.LJ.LJLJ..."
]

game_data5 = [
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJ7F7FJ-",
    "L---JF-JLJ.||-FJLJJ7",
    "|F|F-JF---7F7-L7L|7|",
    "|FFJF7L7F-JF7|JL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L"
]


#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day10.txt", "r")
f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day10.txt", "r")
game_data = f.readlines()

map = BuildMap(game_data)
steps, polygon = traverseMap(map)
print("Total "+ str(steps/2))

print("Inside Loop="+ str(calculateDot(polygon,map)))
