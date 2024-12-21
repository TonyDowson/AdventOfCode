
import re

class Robot:
	maxx = 0
	maxy = 0
	qx = 0
	qy = 0
	
	def __init__(self, s):
		r = s.split()
		pos = re.sub("p=(.*),(.*)","\\1,\\2", r[0]).split(',')
		self.posx = int(pos[0])
		self.posy = int(pos[1])
		vel = re.sub("v=(.*),(.*)","\\1,\\2", r[1]).split(',')
		self.velx = int(vel[0])
		self.vely = int(vel[1])
		
	def __str__(self):
		return "X=" + str(self.posx) + " Y=" + str(self.posy)
		
	def move(self):
		self.posx += self.velx
		self.posy += self.vely
		
	def adjust(self):
		self.posx = self.posx % Robot.maxx
		self.posy = self.posy % Robot.maxy
		
	def quadrant(self):
		if self.posx < Robot.qx and self.posy < Robot.qy:
			return 1
		elif self.posx > Robot.qx and self.posy < Robot.qy:
			return 2
		elif self.posx < Robot.qx and self.posy > Robot.qy:
			return 3
		elif self.posx > Robot.qx and self.posy > Robot.qy:
			return 4
		else:
			return 0
			
gd = [
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3"
]

#gd = ["p=2,4 v=2,-3"]

f = open("Day14.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

robots = []
Robot.maxx = 101
Robot.maxy = 103
Robot.qx = (Robot.maxx - 1) / 2
Robot.qy = (Robot.maxy - 1) / 2
total = 1

for g in game_data:
	robots.append(Robot(g))
	
for i in range(100):
	for r in robots:
		r.move()
		r.adjust()

quads = { 0:0,  1:0, 2:0, 3:0, 4:0 }
for r in robots:
	r.adjust()
	quads[r.quadrant()] += 1
	print(r)

for key,value in quads.items():
	if key != 0:
		total *= value
print(quads)
print(total)
# part 1 229980828
	

