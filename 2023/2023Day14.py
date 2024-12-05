
def rotate90Right(game):
    cols = []

    for i in range(len(game[0])):
        s = ""
        for j in range(len(game)):
            s+=game[j][i]
        cols.append(s)

    return cols

def tilt(game):
    tilted = []
    for s in game:
        new = s
        last = ""
        print("Before=" + s)
        while (new != last):
            last = new
            new = new.replace(".O","O.")            

        tilted.append(last)
        print("After =" + last)

    return tilted

def calculateScore(tilted):
    # time to total
    l = len(tilted)
    total = 0
    for t in tilted:
        l = len(t)        
        for i in range(l):
            if (t[i] == 'O'):
                total += l
            l -= 1
    return total



gd = [
"O....#....\n",
"O.OO#....#\n",
".....##...\n",
"OO.#O....O\n",
".O.....O#.\n",
"O.#..O.#.#\n",
"..O..#O..O\n",
".......O..\n",
"#....###..\n",
"#OO..#....\n"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day14.txt", "r")
gd = f.readlines()

#game_data = []
#for i in gd:
#    game_data.append(i.rstrip('\n'))

game_data = [i.strip('\n') for i in gd]

print("Total = " + str(calculateScore(tilt(rotate90Right(game_data)))))



