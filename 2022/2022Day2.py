f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2022Day2.txt", "r")

# A & X = Rock = 1
# B & Y = Paper = 2
# C & Z = Scissors = 3
# Rock beats Scissors
# Paper beats Rock
# Scissots beats Paper
# 0 for a lost, 3 for a draw, 6 for a win
resultScore = { 'A X':3+1, 
                'A Y':6+2,
                'A Z':0+3,
                'B X':0+1,
                'B Y':3+2, 
                'B Z':6+3,
                'C X':6+1,
                'C Y':0+2,
                'C Z':3+3,
                }

total = 0
for x in f:
  print(x[:3] + ' ' + str(resultScore[x[:3]]))
  total = total + resultScore[x[:3]]

print("Answer is")
print(total)
