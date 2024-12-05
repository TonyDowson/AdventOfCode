def getPriority(letter):
    if (i.isupper()):
        print(x + ' '+ i + ' ' + str(ord(i)-38))
        return ord(i)-38
    else:
        print(x + ' '+ i + ' ' + str(ord(i)-96))
        return ord(i)-96  

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day3.txt", "r")

total = 0

for x in f:
    l = int((len(x)-1)/2)
    first = x[:l]
    second = x[l:]

    for i in first:
      if (second.find(i) >= 0):
        total = total + getPriority(i)
        break

print('Answer is')
print(total)            
        
        

