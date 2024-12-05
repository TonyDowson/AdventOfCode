import re

def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

def getCombination(com,num,max):
    print("getCombination (" +str(com) + "," + str(num) + "," + str(max) + ")")
    newlist = []
    if (num <= max):    
        for c in com:
            new = nth_repl(c, ".","..",num)    
            print("c " + c + " new " + new)   
            newlist.append(c)                     
            newlist.append(new)
        return getCombination(newlist,num+1,max)
    else:
        return com


def getCombinations(game_data):
    for g in game_data:
        p = (g.split(" "))
        pattern = p[0]
        numbers = p[1].split(',')

        print(pattern)
        print(numbers)

        reg = "^\.*"
        for i in range(len(numbers)):
            if (i < len(numbers)-1):
                reg = reg + "[#]{"+str(numbers[i])+"}\.+"            
            else:
                reg = reg + "[#]{"+str(numbers[i])+"}\.*$" 
        print(reg)      


        # crete test
        combinations = []
        test = ""   
        for k in numbers:
            test += "#" * int(k)
            test += "." * 1
        test = test.strip(".")

        # create combinations to test
        combinations.append(test)
        #combinations.append("." + test)        
        #combinations.append(test + ".")              
        #combinations.append("." + test + ".")

        print("Recursion...." + str(getCombination(combinations,1,3)))
        # create more combinations up to len of pattern
        newcombinations = []
        for c in combinations:
            # Take first combination and replace first . with .. and keep doing until end
            newcombinations.append(c)
            dotcount = c.count(".")
            for i in range(1):
                for j in range(1,dotcount+1):
                    new = nth_repl(c, ".","..",j)                    
                    #new = c.replace(".","..",j)    
                    newcombinations.append(new)
            print(newcombinations)                    
        
        
        comcount = 0
        for c in combinations:
            print("Testing " + c)
            if (len(pattern) != len(c)):
                print("no match")
            else:
                m = re.search(reg, c)
                print("Test "+ c + " " + str(m))
                if (m != None):
                    comcount += 1

    return comcount

gd = [
    "???.### 1,1,3\n",
    ".??..??...?##. 1,1,3\n",
    "?#?#?#?#?#?#?#? 1,3,1,6\n",
    "????.#...#... 4,1,1\n",
    "????.######..#####. 1,6,5\n",
    "?###???????? 3,2,1\n"
]
# take numbers and change each one to regex e.g. 1 becomes .#. or ^#. or .#$ and so on

gd = [
    "???.### 1,1,3\n",
]

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day12.txt", "r")
#gd = f.readlines()

game_data = []
for i in gd:
    game_data.append(i.rstrip('\n'))

total = getCombinations(game_data)
print("Total is " + str(total))