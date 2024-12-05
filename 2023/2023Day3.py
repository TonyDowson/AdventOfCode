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
            symbolMap.append((y, (row,col)))
            if (num > 0):
                numberMap.append((num, coords))
                coords = []
                num = 0
        col = col + 1
    row = row + 1

print(numberMap)
print(symbolMap)

for x in numberMap:
    coords = x[1]
    part = False
    for i in coords:
        for j in symbolMap:
            if (abs(j[1][0] - i[0]) <= 1 and abs(j[1][1] - i[1]) <= 1):
                    part = True
                    break
    if (part):
        total = total + x[0]

print ("Answer is")
print(total)