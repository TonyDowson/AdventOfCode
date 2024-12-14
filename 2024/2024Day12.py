	
def update(d,key,value):
	if d.get(key):
		d[key] = d.get(key) + value
	else:
		d[key] = value


def find_regions(vals,regions):
	if len(vals) == 0:
		return regions
	else:
		if len(regions) == 0:
			regions = [ [ vals[0] ] ]
			#print(regions)
		else:
			x = vals[0][0]
			y = vals[0][1]		
			if len(vals) > 1:
				nextx = vals[1][0]
				nexty = vals[1][1]				
			else:
				nextx = -1		
				nexty = -1
			#print("Regions " + str(regions))
			#print("x=" + str(x) + " y=" + str(y))
			newregion = True
			for r in regions:
				for i in r:
					if  (i[0]+1 == x and i[1] == y) or (i[0]==x and i[1]-1 == y) or (i[0]==x and i[1]+1 == y):
						#(i[0]-1==x and  i[1]+1==y) or
						#print("Appending x=" + str(x) + " y=" + str(y))
						r.append((x,y))
						newregion = False
						break
			if newregion:
				regions += [ [ vals[0] ] ]

		return find_regions(vals[1:], regions)

gd = [
	"AAAA",
	"BBCD",
	"BBCC",
	"EEEC"
]

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
print(garden)

# break each into regions
regions = []
newgarden = {}
for key,value in garden.items():
	newgarden[key] = find_regions(value,regions)
#print(newgarden)


total = 0
for key,list in newgarden.items():

	print(key)
	for l in list:
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

print("Perimeter " + str(total))