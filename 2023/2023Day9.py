def newHistory(history):
    #new = [(lambda x: int(history[x+1]) - int(history[x]))(x) for x in range(len(history) - 1)]
    new = []
    allZ = True
    for i in range(len(history) -1):
        diff = int(history[i+1]) - int(history[i])
        new.append(diff)
        if (diff != 0):
            allZ = False

    return new, allZ


def getTotal(game_data):
    total = 0

    for game in game_data:       
        g = [(lambda x: int(x))(x) for x in game.strip("\n").split(' ')]
        history = []

        while True:
            history.append(g)             
            g,z = newHistory(g)
               
            if (z):
                break

        diff = 0
        #diff += (lambda h: diff=h[-1])(h) for h in history
        for h in history:
            diff += h[-1]

        total = total + diff

    return total

game_data = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]

#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day9.txt", "r")
#game_data = f.readlines()

print("Answer is " +  str(getTotal(game_data)))