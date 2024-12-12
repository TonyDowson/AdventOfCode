def remove_leading_zeros(s):
	s1 = s.lstrip('0')
	if s1 == "":
		s1 = "0"
	return s1

def update(d,v,c):
	if d.get(v):
		d[v] += c
	else:
		d[v] = c

gd = "125 17"
gd = "5910927 0 1 47 261223 94788 545 7771"

#f = open("Day11.txt", "r")
#gd = f.readlines()
#game_data = [i.strip('\n') for i in gd]

'''
Original solution
current = gd.split()
for i in range(25):
	new = []
	
	#print(str(i) + " length " + str(len(current)))
	for c in current:
		if c == '0':
			new.append("1")
		elif len(c) % 2 == 0:
			new.append(remove_leading_zeros(c[:int(len(c)/2)]))
			new.append(remove_leading_zeros(c[int(len(c)/2):]))
		else:
			new.append(str(int(c) * 2024))

	#print(new)
	current = new

print("Total part 1= " + str(len(new)))'''

current = {}
for c in gd.split():
	current[c] = 1
print(current) 

for i in range(75):	
	new = {}
	#print(str(i) + " length " + str(len(current)))
	for key,value in current.items():
		if key == '0':
			#new.update("1": value)
			update(new,"1",value)					
		elif len(key) % 2 == 0:
			v1 = remove_leading_zeros(key[:int(len(key)/2)])
			v2 = remove_leading_zeros(key[int(len(key)/2):])
			update(new,v1,value)
			update(new,v2,value)
		else:
			update(new,str(int(key) * 2024),value)				

	current = new

# stone count
print(new)
total = 0
for c in new.items():
	total += c[1]

print("Total is " + str(total))
