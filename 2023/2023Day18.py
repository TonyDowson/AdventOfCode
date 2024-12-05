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
    return step, polygon



game_data = [
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


#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day18.txt", "r")
f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day18.txt", "r")
game_data = f.readlines()

map = BuildMap(game_data)
steps, polygon = traverseMap(map)
print("Total "+ str(steps/2))

print("Inside Loop="+ str(calculateDot(polygon,map)))
