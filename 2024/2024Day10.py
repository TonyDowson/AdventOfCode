
def traverse(maxx, maxy, map, pos, paths):
	if map[pos] == 9:
		paths.append(pos)			
		# paths.add(pos) - if paths is set for part 1
	else:
		v = map[pos]
		# try right
		if pos[0] < maxx:
			newpos = (pos[0]+1,pos[1])
			if map [newpos] == v + 1:
				traverse(maxx, maxy, map, newpos, paths)

		# try left
		if pos[0] > 0:	
			newpos = (pos[0]-1,pos[1])
			if map[newpos] == v + 1:
				traverse(maxx, maxy, map, newpos, paths)

		# try down
		if pos[1] < maxy:			
			newpos = (pos[0],pos[1]+1)
			if map[newpos] == v + 1:
				traverse(maxx, maxy, map, newpos, paths)		

		# try up
		if pos[1] > 0:
			newpos = (pos[0],pos[1]-1)
			if map[newpos] == v + 1:
				traverse(maxx, maxy, map, newpos, paths)	


gd = [
	"89010123",
	"78121874",
	"87430965",
	"96549874",
	"45678903",
	"32019012",
	"01329801",
	"10456732"
]

f = open("Day10.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Build map
y = 0
map = {}
start0 = []
for g in game_data:
	for i in range(len(g)):
		map[(i,y)] = int(g[i])
		if g[i] == '0':
			start0.append((i,y))
	y += 1 

maxx = i
maxy = y-1
print(maxx)
print(maxy)
print(map)
print(start0)


total = 0
for o in start0:
	paths = []
	#paths = set() # change to set for part 1
	#print(o)
	traverse(maxx, maxy, map, o, paths)
	total += len(paths)

print("Total part 2=" + str(total))