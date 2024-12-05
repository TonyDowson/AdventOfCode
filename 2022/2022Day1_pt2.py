f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day1.txt", "r")

subTotal = 0
totalList = []

for x in f:
  if (x[0] != '\n'):
    subTotal = subTotal + int(x)
  else:
    print(subTotal)
    totalList.append(subTotal)
    subTotal = 0

totalList.sort(reverse=True)
total = totalList[0] + totalList[1] + totalList[2]
print(totalList)
print ("Answer is")
print(total)

