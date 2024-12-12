from shapely.geometry import Polygon
	
def update(d,key,value):
	if d.get(key):
		d[key] = d.get(key) + value
	else:
		d[key] = value

gd = [
	"AAAA",
	"BBCD",
	"BBCC",
	"EEEC"
]

#f = open("Day12.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Build map
y = 0
garden = {}
for g in game_data:
	for i in range(len(g)):
		update(garden, g[i],[(i,y)] )
	y += 1 

maxx = i
maxy = y-1
print(maxx)
print(maxy)
print(garden)

total = 0
for key,value in garden.items():
	print(key)
	print(Polygon([(0,0), (4,0), (2,4)]).area)

print("Perimeter " + str(total))