def newHistory(history):
    return [(lambda x: int(history[x+1]) - int(history[x]))(x) for x in range(len(history) - 1)]

def getTotal(game_data):
    total = 0

    for game in game_data:       
        g = [(lambda x: int(x))(x) for x in game.strip("\n").split(' ')]
        history = []

        while not all(element == 0 for element in g):
            history.append(g)             
            g = newHistory(g)

        diff = 0
        #print(history)
        for i in range(len(history)-1,0,-1):
            diff = history[i][0] - diff

        #print("final diff=" + str(diff))        
        total = total + (history[0][0] - diff)

    return total

game_data = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
]

f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day9.txt", "r")
game_data = f.readlines()

print("Answer is " +  str(getTotal(game_data)))