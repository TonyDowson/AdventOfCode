import re

def isValid(pattern,numbers,str):
    if (len(pattern) != len(str)):
        return False
    
    print(pattern)
    print(str)
    Valid = True
    broken = 0
    n = []
    for i in range(len(pattern)):
        print("Pattern=" + pattern[i] + " str=" + str[i])
        if ((pattern[i] == "?" or pattern[i] == "#") and str[i] == "#"):
            broken += 1
            if (i > 0 and str[i-1] != '.'):
                Valid = False
                break
            if (i < len(str) and str[i+1] != '.'):
                Valid = False
                break 
        elif ((pattern[i] == "." or pattern[i] == "?") and str[i] == "."):
            if (broken > 0):
                n.append(broken)
                broken = 0
        elif (pattern[i] != str[i]):
            Valid = False
            break 

    if (broken > 0):
        n.append(broken)        

    print(n)
    print(numbers)

    return Valid


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

        combinations = []
        test = ""   
        for k in numbers:
            test += "#" * int(k)
            test += "." * 1
                
        test = test.strip(".")
        #print(test)

        #print(isValid(pattern,numbers,test))


        combinations.append(test)
        combinations.append("." + test)        
        combinations.append(test + ".")              
        combinations.append("." + test + ".")

        # create more combinations up to len of pattern
        newcombinations = []
        for c in combinations:
            # Take first combination and replace first . with .. and keep doing until end
            newcombinations.append(c)
            dotcount = c.count(".")
            for i in range(1):
                for j in range(1,dotcount+1):
                    new = c.replace(".","..",j)
                    #if (len(pattern) != len(c)):        
                    newcombinations.append(new)
            print(newcombinations)                    
        
        # now add a . at the start

        # take spring numbers and create a string which is base string
        # if length is same as spring_format then job done
        # if length is less as spring_format then add . after first dot and then next . etc

        # Replace first with # and rest with . - check if it conforms
        # replace first with . and second with # and rest with . - check if it conforms
        
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