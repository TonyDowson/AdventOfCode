import numpy as np
import math
import re

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
	"Button A: X+69, Y+23\n",
	"Button B: X+27, Y+71\n",
	"Prize: X=18641, Y=10279\n"
]

f = open("Day13.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

total = 0
for g in game_data:
    if g.find("Button A:") != -1:
        buttonA = g.split(' ')
    if g.find("Button B:") != -1:
        buttonB = g.split()   
    if g.find("Prize") != -1:
        prize = g.split()

        x1 = int(re.sub("X\+(.*),","\\1",buttonA[2]))
        x2 = int(re.sub("X\+(.*),","\\1",buttonB[2]))
        y1 = int(re.sub("Y\+","",buttonA[3]))
        y2 = int(re.sub("Y\+","",buttonB[3]))

        x = int(re.sub("X=(.*),","\\1",prize[1])) + 10000000000000
        y = int(re.sub("Y=","",prize[2])) + 10000000000000
        A = np.array([[x1,x2], [y1,y2]])
        B = np.array([x,y])
        r1, r2 = np.linalg.solve(A, B)
        print(r1,r2)
        buttonA_result = math.modf(r1)
        buttonB_result = math.modf(r2)
        r4 = math.modf(r2)
         
		# check result
        if (buttonA_result[1] > 0 and buttonA_result[1] <= 10000000000000) and (buttonA_result[0] > 0.999 or buttonA_result[0] < 0.001) and \
            (buttonB_result[1] > 0 and buttonB_result[1] <= 10000000000000) and (buttonB_result[0] > 0.999 or buttonB_result[0] < 0.001):
            print("Good")
            if buttonA_result[0] > 0.999:
                total += 3
            if buttonB_result[0] > 0.999:
                total += 1
            total += (buttonA_result[1] * 3)
            total += buttonB_result[1]

            
print(total)
# part 1
# 19231 too low
# 24809 too low
# 25705 too low

# part 2
# 108528956728655