f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day1.txt", "r")

total = 0

for x in f:
    stripped = x.lower().strip('abcdefghijklmnopqrstuvwxyz\n')

    print(stripped)
    if (len(stripped) == 1):
       num = (int(stripped[0]) * 10) + int(stripped[0])
    else:
       num = (int(stripped[0]) * 10) + (int(stripped[-1]))
    print(num)
    total = total + num

print ("Answer is")
print(total)
