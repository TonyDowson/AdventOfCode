f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day1.txt", "r")

total = 0

for x in f:
    textToNumber = x.replace("one","o1e").replace("five","f5e").replace("three","t3e").replace("seven","s7n").replace("nine","n9e").replace("eight","e8t").replace("two","t2o").replace("six","s6x").replace("four","f4r")
    stripped = textToNumber.lower().strip('abcdefghijklmnopqrstuvwxyz\n')

    if (len(stripped) == 1):
       num = (int(stripped[0]) * 10) + int(stripped[0])
    else:
       num = (int(stripped[0]) * 10) + (int(stripped[-1]))

    print(x + "->" + textToNumber + "->" + stripped + "->" + str(num))
    total = total + num

print ("Answer is")
print(total)
