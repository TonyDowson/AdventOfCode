from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def calculateArea(coords):
    area = 0
    minrow, mincol = 0,0
    maxrow, maxcol = 0,0    

    for c in coords:
        row = c[0]
        col = c[1]
        if (row > maxrow):
            maxrow = row
        if (col > maxcol):
            maxcol = col
        if (row < minrow):
            minrow = row
        if (col < mincol):
            mincol = col          

    print("minrow="+str(minrow) + " maxrow="+str(maxrow))
    print("mincol="+str(mincol) + " maxcol="+str(maxcol))    
    print(coords)
    polygon = Polygon(coords) 
    for row in range(minrow, maxrow):
        for col in range(mincol, maxcol):
            point = Point(row, col)
            if (polygon.within(point)):
                area+= 1    
    print("Polygon area "+str(polygon.area))
    print("area calced="+str(area))         
    return area    


def createMap(game_data):
    row, col = 0,0
    maxrow, maxcol = 0,0
    perimeter = 0
    coords = [ (row, col ) ]
    for i in game_data:
        dir, move, colour = i.split(' ')
        if dir == 'U':
            row -= int(move)
        elif dir == 'D':
            row += int(move)
        elif dir == 'L':
            col -= int(move)
        elif dir == 'R':
            col += int(move)
        else:
            AssertionError
        perimeter += int(move)
        coords.append( (row, col ) )          

    return coords, perimeter

def traverseMap(map):
    step = 0
    polygon = []
    return step, polygon


game_data = [
    "R 6 (#70c710)\n",
    "D 5 (#0dc571)\n",
    "L 2 (#5713f0)\n",
    "D 2 (#d2c081)\n",
    "R 2 (#59c680)\n",
    "D 2 (#411b91)\n",
    "L 5 (#8ceee2)\n",
    "U 2 (#caa173)\n",
    "L 1 (#1b58a2)\n",
    "U 2 (#caa171)\n",
    "R 2 (#7807d2)\n",
    "U 3 (#a77fa3)\n",
    "L 2 (#015232)\n",
    "U 2 (#7a21e3)\n"
]


#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day18.txt", "r")
#f = open("2023Day18.txt", "r")
#game_data = f.readlines()

coords, perimeter = createMap(game_data)
print("Area="+ str(calculateArea(coords)+perimeter))

#steps, polygon = traverseMap(map)
#print("Total "+ str(steps/2))


