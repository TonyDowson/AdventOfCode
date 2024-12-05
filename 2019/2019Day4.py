import math

def sortFunc(e):
  return abs(e[0]) + abs(e[1])

def validPassword_pt1(n):
    increasing = True
    adjacentDigits = False
    num = str(n)    
    lastnum = 0

    for i in num:
        digit = int(i)
        if (digit < lastnum):
            increasing = False
        if (digit == lastnum):
            adjacentDigits = True

        lastnum = digit            

    return (increasing and adjacentDigits)

def validPassword_pt2(n):
    increasing = True
    adjacentDigits = False
    num = str(n)    
    last_digit = 0
    lastnum = 0    

    # parse number and produce a list
    l = []
    for i in num:
        digit = int(i)
        if (digit == last_digit):
            pop_num = l.pop()            
            l.append((pop_num * 10) + digit)
        else:
            l.append(digit)
            last_digit = digit  

        if (digit < lastnum):
            increasing = False

        lastnum = digit                            

    for i in l:
        if (i > 10 and i < 100):
            adjacentDigits = True          

    return (increasing and adjacentDigits)

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day2.txt", "r")
#gd = f.readlines()
#game_data = [i.strip('\n') for i in gd]
valid_passwords1 = 0

for i in range(158126,624574):
    #print("Testing "+str(i))
    if (validPassword_pt1(i)):
        #print(str(i) + " is valid")
        valid_passwords1 += 1      

valid_passwords2 = 0
#for i in [112233,123444,111122]:
for i in range(158126,624574):
    #print("Testing "+str(i))
    if (validPassword_pt2(i)):
        print(str(i) + " is valid")
        valid_passwords2 += 1        

print("Part 1 - Answer is " + str(valid_passwords1))
print("Part 2 - Answer is " + str(valid_passwords2))
