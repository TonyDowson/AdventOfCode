import re

def isValid(test, pattern):
    spring = 0
    l = []
    for i in test:
        if (i == "#"):
            spring  += 1
        elif (i == "."):
            if (spring > 0):
                l.append(spring)
            spring = 0
    if (spring > 0):
        l.append(spring)     

    return l == pattern

def check_existence(text):
    return bool(re.search(r'[?]', text))

def createTestCombinations(l):
    new = []
    for i in l:
        new.append(i.replace('?','#',1))
        new.append(i.replace('?','.',1))

    if (check_existence(new[0])): 
        return createTestCombinations(new)

    return new        

def getCombinations(puzzle,n):
    springs, p = puzzle.split(' ')
    #pattern = [int(x) for x in p.split(',')*n]
    #springs = ((s+'*')*n).rstrip('*').replace('*','?')
    pattern = [int(x) for x in p.split(',')]
    #print(pattern)
    #print(springs)

    # create tests combinations
    combinations = createTestCombinations([springs])

    # Test test combinations
    valid = 0
    validcombinations = []
    for c in combinations:
        if (isValid(c,pattern) and len(springs) == len(c)):
            valid += 1
            validcombinations.append(c)
    
    if (n == 1):
        return valid
    multiple = []       
    for c1 in validcombinations:
        for c2 in validcombinations:
            multiple.append(c1+'?'+c2)

    multiplecombinations = createTestCombinations(multiple)
    #print(multiplecombinations)        
    for c in multiplecombinations:
        if (isValid(c,pattern) and len(springs) == len(c)):
            valid += 1
              
    return valid


game_data = [
    "???.### 1,1,3\n",
    ".??..??...?##. 1,1,3\n",
    "?#?#?#?#?#?#?#? 1,3,1,6\n",
    "????.#...#... 4,1,1\n",
    "????.######..#####. 1,6,5\n",
    "?###???????? 3,2,1\n",
]

#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day12.txt", "r")
#game_data = f.readlines()

total = 0
for g in game_data:
    g1 = g.strip('\n')
    print(g1)
    valid1 = getCombinations(g1,1)
    print(g1 + " - " + str(valid1) + " arrangements * 1")    
    valid2 = getCombinations(g1,2)  
    print(g1 + " - " + str(valid2) + " arrangements * 2")    
    valid3 = int(valid1 * pow(valid2,4 ))
    print(g1 + " - " + str(valid3) + " arrangements * 5")
    total += valid1

print(total)
