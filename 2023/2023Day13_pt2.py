
def getColumns(game):
    cols = []

    for i in range(len(game[0])):
        s = ""
        for j in range(len(game)):
            s+=game[j][i]
        cols.append(s)

    return cols

def equals(str1,str2,smudge):
    diff = 0

    if (str1 and str2):
        for i in range(len(str1)):
            if (str1[i] != str2[i]):
                diff += 1
        if (diff < (1 + smudge)):
            if (diff == 0):
                return True, 1
            else:
                return True, 0
        else:
            return False, diff            
    else:
        return False, diff


def findReflection(board):
    num = 0
    prevrow = ""
    reflect = False

    ref = []

    for g in board:
        print("Comparing prev="+ prevrow + " current=" +g)
        eq,smudgeleft = equals(g, prevrow,1)        
        if (eq):
            print("Possible reflection " + str(num))
            reflect = True
            ref.append((num, smudgeleft))
            
        prevrow = g
        num += 1

    # confirm its a relection
    print(ref)
    for r in ref:
        reflect = True
        num = r[0]
        smudgeleft = 1
        j = 1
        for i in range(num-1,-1,-1):
            if ((i+j) < len(board)):
                print("comparing " + board[i] + " " + board[i+j])
            if ((i+j) < len(board)):
                eq,smudge = equals(board[i],board[i+j],smudgeleft)
                if (smudge == 0):
                    smudgeleft = 0
                if (not eq):
                    print("NOPE !")
                    reflect = False
                    break
            j += 2
        print("smudge left="+str(smudgeleft))        
        if (smudgeleft > 0):
            reflect = False
        if (reflect):
            break

    return reflect,num


def getTotalRowsFirst(rows,cols):
    # find 2 rows that match
    print("rows " + str(rows))
    print("cols " + str(cols))
    subtotal = 0

    print("Doing Rows")
    reflect, num = findReflection(rows)
    if (reflect):
        subtotal = num * 100
    else:
        print("Doing Cols")
        reflect, num = findReflection(cols)
        if (reflect):
            subtotal = num
        else:
            print("NO REFLECTION DETECTED")
            exit
    
    return subtotal

def getTotalColsFirst(rows,cols):
    # find 2 rows that match
    print("rows " + str(rows))
    print("cols " + str(cols))
    subtotal = 0

    print("Doing Cols")
    reflect, num = findReflection(cols)
    if (reflect):
        subtotal = num
    else:
        print("Doing Rows")
        reflect, num = findReflection(rows)
        if (reflect):
            subtotal = num * 100
        else:
            print("NO REFLECTION DETECTED")
            exit
    
    return subtotal

game_data = [
    "#.##..##.\n",
    "..#.##.#.\n",
    "##......#\n",
    "##......#\n",
    "..#.##.#.\n",
    "..##..##.\n",
    "#.#.##.#.\n",
    "\n",
    "#...##..#\n",
    "#....#..#\n",
    "..##..###\n",
    "#####.##.\n",
    "#####.##.\n",
    "..##..###\n",
    "#....#..#\n"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day13.txt", "r")
game_data = f.readlines()

game = []
total = 0
for i in game_data:
    if (i == '\n'):
        total += getTotalRowsFirst(game,getColumns(game))
        game = []
    else:
        game.append(i.rstrip('\n'))

if (game):
    total += getTotalRowsFirst(game,getColumns(game))

game = []
total2 = 0
for i in game_data:
    if (i == '\n'):
        total2 += getTotalColsFirst(game,getColumns(game))
        game = []
    else:
        game.append(i.rstrip('\n'))

if (game):
    total2 += getTotalColsFirst(game,getColumns(game))

print(total)
print(total2)
