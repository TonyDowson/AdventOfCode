f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day1.txt", "r")

subTotal = 0
maxTotal = 0

for x in f:
  if (x[0] != '\n'):
    subTotal = subTotal + int(x)
  else:
    print(subTotal)
    if (subTotal > maxTotal):
      maxTotal = subTotal
    subTotal = 0

print ("Answer is")
print(maxTotal)
