f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day2.txt", "r")

# A & X = Rock = 1
# B & Y = Paper = 2
# C & Z = Scissors = 3
# Rock beats Scissors
# Paper beats Rock
# Scissots beats Paper
# 0 for a lost, 3 for a draw, 6 for a win
resultScore = { 'A X':3+0, 
                'A Y':1+3,
                'A Z':2+6,
                'B X':1+0,
                'B Y':2+3, 
                'B Z':3+6,
                'C X':2+0,
                'C Y':3+3,
                'C Z':1+6,
                }

total = 0
for x in f:
  print(x[:3] + ' ' + str(resultScore[x[:3]]))
  total = total + resultScore[x[:3]]

print("Answer is")
print(total)
