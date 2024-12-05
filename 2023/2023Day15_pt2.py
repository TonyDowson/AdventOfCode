

def calculateHash(value):
    hash = 0
    for s in value:
        hash += ord(s)
        hash *= 17
        hash = hash % 256

    return hash





gd = "HASH\n"
gd = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n"

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day15.txt", "r")
gd = f.readline()

print(gd)
total = 0
for g in gd.rstrip('\n').split(','):
    h = calculateHash(g)
    total += h
    print("Hash value is "+ str(h))

print("Total " + str(total))


