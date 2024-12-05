f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day4.txt", "r")

def getMoreWinningCard(cards,orig):
    newCards = []
    for i in range(len(cards)):
        #print(str(i) + str(cards[i]))
        num = cards[i][1]
        cardnum = cards[i][0]
        if (num > 0):
            newCards.extend(orig[cardnum:cardnum+num])            
            #print("Get " + str(num) + " cards " + str(orig[cardnum:cardnum+num]))
            #for j in range(cardnum,cardnum+num):
            #    newCards.append(orig[j])

    #newCards.sort()
    return newCards

    
total = 0
cards = []
for x in f:
    p = x.replace("\n","").replace(":","|").split("|")
    
    winningNumbers = p[1].split()
    myNumbers = p[2].split()

    #print("Card " + p[0].split()[1])
    #print("Winning Numbers " + str(winningNumbers))
    #print("My Numbers " + str(myNumbers))

    winners = 0
    for i in myNumbers:
        if (i in winningNumbers):
            winners = winners + 1
    print("Card " + p[0].split()[1] + " has " + str(winners) + " winners")

    cards.append( (int(p[0].split()[1]), winners) )

print("Cards " + str(cards))

new = cards
all = cards

while new:
    new = getMoreWinningCard(new, cards)
    if (new):
        print("More Winning Cards " + str(new[0]))
        all.extend(new)

total = len(all)
print ("\nAnswer is " + str(total))
