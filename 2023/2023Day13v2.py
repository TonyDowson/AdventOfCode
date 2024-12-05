
def getColumns(game):
    cols = []

    for i in range(len(game[0])):
        s = ""
        for j in range(len(game)):
            s+=game[j][i]
        cols.append(s)

    return cols

def equals(str1,str2):
    return (str1 == str2)

def findReflection(board):
    num = 0
    prevrow = ""
    reflect = False

    ref = []

    for g in board:
        print("Comparing prev="+ prevrow + " current=" +g)
        if (equals(g,prevrow)):
            print("Possible reflection " + str(num))
            reflect = True
            ref.append(num)
            
        prevrow = g
        num += 1

    # confirm its a relection
    for r in ref:
        reflect = True
        num = r
        j = 1
        for i in range(num-1,-1,-1):
            if ((i+j) < len(board)):
                print("comparing " + board[i] + " " + board[i+j])
            if (((i+j) < len(board)) and not equals(board[i],board[i+j]) ):
                print("NOPE !")
                reflect = False
                break
            j += 2
        if (reflect):
            break

    return reflect,num


def getTotal(rows,cols):
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

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day13.txt", "r")
#game_data = f.readlines()

game = []
total = 0
for i in game_data:
    if (i == '\n'):
        total += getTotal(game,getColumns(game))
        game = []
    else:
        game.append(i.rstrip('\n'))

if (game):
    total += getTotal(game,getColumns(game))

print(total)
