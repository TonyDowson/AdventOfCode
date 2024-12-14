import numpy as np

class Claw:
    def __init__(self,buttonA, buttonB, prize):
        self.buttonA = buttonA
        self.buttonB = buttonB
		self.price 
        
	def solve(self):
		A = np.array([[94,22], [34,67]])
		B = np.array([8400,5400])
		C = np.linalg.solve(A, B)

gd = [
	"Button A: X+94, Y+34\n",
	"Button B: X+22, Y+67\n",
	"Prize: X=8400, Y=5400\n",
	"\n",
	"Button A: X+26, Y+66\n",
	"Button B: X+67, Y+21\n",
	"Prize: X=12748, Y=12176\n",
	"\n",
	"Button A: X+17, Y+86\n",
	"Button B: X+84, Y+37\n",
	"Prize: X=7870, Y=6450\n",
	"\n",
	"Button A: X+69, Y+23\n"
	"Button B: X+27, Y+71\n",
	"Prize: X=18641, Y=10279\n"
]

#f = open("Day13.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]


for g in game_data:
    if g.find("Button A") != -1:
		
