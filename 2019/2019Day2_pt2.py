import math

def execute(all_data,program):
    #print("Prog..." + str(program))
    if (program[0] == 1):
        all_data[program[3]] = all_data[program[1]] + all_data[program[2]]
    elif (program[0] == 2):
        all_data[program[3]] = all_data[program[1]] * all_data[program[2]]   
    elif (program[0] == 99):       
        print("END")              
    else:
        print("ERROR")

    return all_data

gd = [1,9,10,3,2,3,11,0,99,30,40,50]
gd4 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,6,23,2,13,23,27,1,27,13,31,1,9,31,35,1,35,9,39,1,39,5,43,2,6,43,47,1,47,6,51,2,51,9,55,2,55,13,59,1,59,6,63,1,10,63,67,2,67,9,71,2,6,71,75,1,75,5,79,2,79,10,83,1,5,83,87,2,9,87,91,1,5,91,95,2,13,95,99,1,99,10,103,1,103,2,107,1,107,6,0,99,2,14,0,0]
#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day2.txt", "r")
#gd = f.readlines()
#game_data = [i.strip('\n') for i in gd]
game_data = gd4
print("Starting with..." + str(game_data))
finished = False

for n in range(0,99):
    for v in range(0,99):
        print("Noun=" + str(n) + " Verb="+str(v))        
        game_data = list(gd4)
        game_data[1] = n
        game_data[2] = v
        for i in range(0,len(game_data),4):
            prog = game_data[i:i+4]
            if (prog[0] != 99):
                game_data = execute(game_data,prog)
            else:
                break
            if (game_data[0] == 19690720):
                print("Noun=" + str(n) + " Verb="+str(v))
                finished = True
                break

        if finished:
            break   
    if finished:
        break           

print("Pos 0 "+ str(game_data[0]))
print("Noun=" + str(n) + " Verb="+str(v))
print("Answer "+ str((n * 100) + v))