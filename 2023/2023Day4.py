f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day4_sample.txt", "r")

total = 0
for x in f:
    p = x.replace("\n","").replace(":","|").split("|")
    
    winningNumbers = p[1].split()
    myNumbers = p[2].split()

    print("Card " + p[0].split()[1])
    print("Winning Numbers " + str(winningNumbers))
    print("My Numbers " + str(myNumbers))

    subtotal = 0
    for i in myNumbers:
        if (i in winningNumbers):
            if (subtotal == 0):
                subtotal = 1
            else:
                subtotal = subtotal * 2
    print(p[0] + " is worth " + str(subtotal))
    total = total + subtotal

print ("\nAnswer is " + str(total))
