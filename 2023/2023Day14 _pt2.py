
def flip(game):
    new = []

    for i in range(len(game[0])):
        s = ""
        for j in range(len(game)):
            s+=game[j][i]
        new.append(s)

    return new


def reverse(game):
    new = []

    for g in game:
        new.append(g[::-1])

    return new


def tilt(game):
    tilted = []
    for s in game:
        new = s
        last = ""
        while (new != last):
            last = new
            new = new.replace(".O","O.")            

        tilted.append(last)
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

b = []
for i in gd:
    b.append(i.rstrip('\n'))


for i in range(1000):
    #print("Before "+ str(b))
    b = flip(b)
    #print("Board from North"+str(b))       
    print("Before North tilt score =" + str(calculateScore(b) ) )   
    score = calculateScore(b)         
    if (score == 95273):
        print("SCORE IS 95273")
    b = tilt(b)
    #print("After North tilt "+str(b)) 

    b = flip(b) 
    #print("Board back to normal "+str(b))   
    b = tilt(b)      
    #print("After West tilt "+str(b))        

    b = flip(b) 
    b = reverse(b)
    #print("Board from South "+str(b))       
    b = tilt(b)     
    #print("After South tilt "+str(b))             

    b = reverse(b)
    b = flip(b) 
    b = reverse(b)    
    #print("Board from East "+str(b))    
    b = tilt(b)     
    #print("After East tilt "+str(b))          

    b = reverse(b)                
   
    #print("Board after " + str(i+1) +" score="+ str(score) + " " +str(b)) 
    #print("Board after " + str(i+1) +" score="+ str(score))     
    
print("Total = " + str(calculateScore(b)))
