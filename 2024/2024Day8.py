def check(maxx, maxy, x, y):
	if x >= 0 and y >= 0 and x <= maxx and y < maxy:
		return (x,y)
	else:
		return None
	
gd = [
	'............',
	'........0...',
	'.....0......',
	'.......0....',
	'....0.......',
	'......A.....',
	'............',
	'............',
	'........A...',
	'.........A..',
	'............',
	'............'
]

f = open("Day8.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

y = 0
map = {}
for g in game_data:
	for i in range(len(g)):
		if g[i] != '.':
			if map.get(g[i]) is None:
				map[g[i]] = [(i,y)]
			else:
				map[g[i]].append((i,y))
	y += 1
	
maxy = y
maxx = i

print(map)
print(maxx)
print(maxy)

anti = set()
for m in map.items():
	coords = m[1]
	for c in range(len(coords)):
		left = coords[c+1:]
		for i in left:
			a1 = coords[c]
			print(str(a1) + '-' + str(i))
			xdist = a1[0] - i[0]
			ydist = a1[1] - i[1]
			print('xdist='+str(xdist) + ' ydist'+str(ydist))
			anti.add((a1[0]+xdist,a1[1]+ydist))
			anti.add((i[0]-xdist,i[1]-ydist))
			
anti2 = {check(maxx, maxy, i[0], i[1]) for i in anti}
print('Total part 1')			
print(len(anti2)-1)
print(maxx)
print(maxy)

#part 2...copy and paste development
anti = set()
for m in map.items():
	coords = m[1]
	for c in range(len(coords)):
		left = coords[c+1:]
		for i in left:
			a1 = coords[c]
			print(str(a1) + '-' + str(i))
			xdist = a1[0] - i[0]
			ydist = a1[1] - i[1]
			print('xdist='+str(xdist) + ' ydist'+str(ydist))
			
			# super brute brute force again... Tony 'brute' Dowson
			for j in range(maxx):
				anti.add((a1[0]+(xdist*j),a1[1]+(j*ydist)))
				anti.add((i[0]-(j*xdist),i[1]-(j*ydist)))

anti2 = {check(maxx, maxy, i[0], i[1]) for i in anti}
print('Total part 2')			
print(len(anti2)-1)

