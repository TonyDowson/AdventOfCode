# Functions
def getPriority(letter):
    if (letter.isupper()):
        print(letter + ' ' + str(ord(letter)-38))
        return ord(letter)-38
    else:
        print(letter + ' ' + str(ord(letter)-96))
        return ord(letter)-96  
    
def isLetterInRucksack(letter, rucksack):
    if (rucksack.find(letter) >= 0):
        return True
    else:
        return False

# Open and read file into list
f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day3.txt", "r")
rucksacks = f.readlines()
l = len(rucksacks)
total = 0

for i in range(0,l,3):
    rucksack3 = rucksacks[i:i+3]
    
    for j in rucksack3[0]:
        if (isLetterInRucksack(j,rucksack3[1])):
            if (isLetterInRucksack(j,rucksack3[2])): 
                print('Common item is ' + j)
                total = total + getPriority(j)
                break

# Answer total
print('Answer is')
print(total)