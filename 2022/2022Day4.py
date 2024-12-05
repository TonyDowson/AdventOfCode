f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day4.txt", "r")

total = 0

for x in f:
    l = x.find(',')
    range1 = x[:l]
    range2 = x[l+1:]

    i = range1.find('-')
    sectionid1_lower = int(range1[:i])
    sectionid1_upper = int(range1[i+1:])
    
    i = range2.find('-')
    sectionid2_lower = int(range2[:i])
    sectionid2_upper = int(range2[i+1:])

    if ((sectionid1_lower >= sectionid2_lower and sectionid1_upper <= sectionid2_upper) or
        (sectionid2_lower >= sectionid1_lower and sectionid2_upper <= sectionid1_upper)):
        print(x + "YES")
        total = total + 1
    else:
        print(x + "NO")




print('Answer is')
print(total)            
        
        

