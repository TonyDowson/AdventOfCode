f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day2.txt", "r")

total = 0

for x in f:
    games = x.replace('\n','').split(':')
    reveals = games[1].replace(';',',').split(',')
    gameid = int((games[0].split())[1])
    red = 0
    blue = 0
    green = 0

    for i in reveals:
        reveal = i.split()
        if (reveal[1] == 'red' and int(reveal[0]) > red):
            red = int(reveal[0])
        elif (reveal[1] == 'green' and int(reveal[0]) > green):
            green = int(reveal[0])
        elif (reveal[1] == 'blue' and int(reveal[0]) > blue):
            blue = int(reveal[0])          
    
    total = total + (red * blue * green)

print ("Answer is")
print(total)