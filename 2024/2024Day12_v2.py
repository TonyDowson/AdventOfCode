def traverse(maxx, maxy, map, pos, paths):
	paths.append(pos)
	v = map[pos]
	# try right
	if pos[0] < maxx:
		newpos = (pos[0]+1,pos[1])
		if map [newpos] == v and newpos not in paths:
			traverse(maxx, maxy, map, newpos, paths)

	# try left
	if pos[0] > 0:	
		newpos = (pos[0]-1,pos[1])
		if map[newpos] == v and newpos not in paths:
			traverse(maxx, maxy, map, newpos, paths)

	# try down
	if pos[1] < maxy:			
		newpos = (pos[0],pos[1]+1)
		if map[newpos] == v and newpos not in paths:
			traverse(maxx, maxy, map, newpos, paths)		

	# try up
	if pos[1] > 0:
		newpos = (pos[0],pos[1]-1)
		if map[newpos] == v and newpos not in paths:
			traverse(maxx, maxy, map, newpos, paths)

gd = [
	"AAAA",
	"BBCD",
	"BBCC",
	"EEEC"
]
'''
gd = [
	"OOOOO",
	"OXOXO",
	"OOOOO",
	"OXOXO",
	"OOOOO"
]

gd = [
"RRRRIICCFF",
"RRRRIICCCF",
"VVRRRCCFFF",
"VVRCCCJFFF",
"VVVVCJJCFE",
"VVIVCCJJEE",
"VVIIICJJEE",
"MIIIIIJJEE",
"MIIISIJEEE",
"MMMISSJEEE"
]
'''

#f = open("Day12.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Build garden
y = 0
garden = {}
for g in game_data:
	for x in range(len(g)):
		garden[(x,y)] = g[x]
	y += 1 
print(garden)

maxx = x
maxy = y-1

all = []
for key,value in garden.items():
	polygon = []
	traverse(maxx, maxy, garden, key, polygon)
	found = False
	for i in all:
		if key in i:
			found = True
			break
	if not found:
		all.append(polygon)
		#print(polygon)
print(all)
	
total = 0
for l in all:
	print(l)
	per = 0
	for c in l:
		per += 4
		if (c[0] - 1, c[1]) in l:
			per -= 1
		if (c[0] + 1, c[1]) in l:
			per -= 1
		if (c[0], c[1] - 1) in l:	
			per -= 1	
		if (c[0], c[1] + 1) in l:	
			per -= 1
	print("area="+str(len(l)) + " perimeter="+str(per))
	total += len(l) * per

print("Part 1 Total " + str(total))
print()
total = 0
for l in all:
	print(l)
	sides = 4
	if len(l) <= 2:
		sides = 4
	print("area="+str(len(l)) + " sides="+str(sides))
	total += len(l) * sides

print("Part 2 Total " + str(total))
