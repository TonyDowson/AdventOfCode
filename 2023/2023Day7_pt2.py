
from datetime import datetime

def getRank(hand):
    #d = {k:v for k,v in zip(hand,[1,1,1,1,1])}    
    d = {}
    for x in hand:
        v = d.get(x,0)
        d[x] = v + 1

    pair = 0
    three = 0
    four = 0
    five = 0

    for key in d:
        if (key != "J"):
            if (d[key] == 2):       
                pair = pair + 1
            elif (d[key] == 3):        
                three = 1
            elif (d[key] == 4):      
                four = 1
            elif (d[key] == 5):
                five = 1

    j = d.get("J",0)
    for i in range(j):
        if (four == 1):
            five = 1
            four = 0
        elif (three == 1):
            four = 1            
            three = 0
        elif (pair == 2):
            pair = 1
            three = 1
        elif (pair == 1):
            three = 1
            pair = 0
        else:
            pair = 1

    if (five == 1):
        order = "1" + getHandValue(hand)
    elif (four == 1):
        order = "2" + getHandValue(hand)
    elif (three == 1 and pair == 1):
        order = "3" + getHandValue(hand)
    elif (three == 1):
        order = "4" + getHandValue(hand)        
    elif (pair == 2):
        order = "5" + getHandValue(hand)
    elif (pair == 1):
        order = "6" + getHandValue(hand)
    else:
        order = "7" + getHandValue(hand)

    return order

def getHandValue(hand):
    return hand.replace("K","B").replace("Q","C").replace("J","Z").replace("T","E").replace("9","F").replace("8","G").replace("7","H").replace("6","I").replace("5","J").replace("4","K").replace("3","L").replace("2","M")

def myFunc(e):
  return e[1]


f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day7.txt", "r")
total = 0
hands = []

print(datetime.now())
for x in f:
    h = x.replace('\n','').split(' ')
    hands.append( (h[0], getRank(h[0]),  int(h[1])) )

hands.sort(reverse=True, key=myFunc)

for i in range(0,len(hands)):
    total = total + ((i+1) * hands[i][2])

print ("Answer is " + str(total))
print(datetime.now())