f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day3.txt", "r")

total = 0
numberMap = []
symbolMap = []
row=0

# Build maps
for x in f:
    print(x)
    coords = []
    num = 0
    col = 0
    x = x +'.'
    for y in x:
        if (y.isdigit()):
            num = (num * 10) + int(y)
            coords.append((row,col))
        elif (y == '.'):
            if (num > 0):
                numberMap.append((num, coords))
                coords = []
                num = 0
        elif (y != '\n'): #must be a symbol
            if (y == '*'):
                symbolMap.append((y, (row,col)))
            if (num > 0):
                numberMap.append((num, coords))
                coords = []
                num = 0
        col = col + 1
    row = row + 1

print(numberMap)
print(symbolMap)

for j in symbolMap:
    print(j)
    firstpart = False    
    for x in numberMap:
        coords = x[1]
        secondpart = False

        if (not firstpart):
            for i in coords:
                if (abs(j[1][0] - i[0]) <= 1 and abs(j[1][1] - i[1]) <= 1):
                    firstpart = True
                    break          
                
            if (firstpart):
                num1 = x[0]
                #print("num1 " + str(num1))
                continue

        for i in coords:
            if (abs(j[1][0] - i[0]) <= 1 and abs(j[1][1] - i[1]) <= 1):
                    secondpart = True
                    break          
            
        if (secondpart):
            num2 = x[0]
            #print("num2 " + str(num2))
            break

    if (firstpart and secondpart):
        total = total + (num1 * num2)

print ("Answer is")
print(total)