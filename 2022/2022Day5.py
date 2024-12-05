f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day5.txt", "r")

stacks = { 1:[], 2:[], 3:[],4:[],5:[],6:[],7:[],8:[],9:[] }
total = 0

for x in f:
    # Create a dictionary of lists
    l = len(x)
    if (l == 1):
        break

    for i in range(1,l,4):
        stack = int((i-1)/4)+1
        if (x[i].isalpha()):
            stacks[stack].insert(0,x[i])
            print(x[i])

print(stacks)

for x in f:
    print(x)
    craneMove = x.split()
    
    print(craneMove)
    for i in range(0,int(craneMove[1])):
        stacks[int(craneMove[5])].append(stacks[int(craneMove[3])].pop())
    print(stacks)

print('Answer is')
for i in range(1,10):
    print(stacks[i].pop())

        
        

