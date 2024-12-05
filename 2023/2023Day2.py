f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day2.txt", "r")

total = 0

for x in f:
    games = x.replace('\n','').split(':')
    reveals = games[1].replace(';',',').split(',')
    gameid = int((games[0].split())[1])
    possible = True

    for i in reveals:
        reveal = i.split()
        if (reveal[1] == 'red' and int(reveal[0]) > 12):
            possible = False
        elif (reveal[1] == 'green' and int(reveal[0]) > 13):
            possible = False
        elif (reveal[1] == 'blue' and int(reveal[0]) > 14):
            possible = False            
    
    if (possible):
        total = total + gameid

print ("Answer is")
print(total)