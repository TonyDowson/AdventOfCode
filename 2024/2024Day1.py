def part1(l1,l2):
   dist = 0
   for i in range(len(l1)):
      dist += abs(int(l1[i]) - int(l2[i]))

   print(dist)

def part2(l1,l2):
   similar = 0
   for i in l1:
      count = 0      
      for j in l2:
         if i == j:
            count += 1
      
      similar += int(i) * count

   print(similar)

gd = [
"3   4\n",
"4   3\n",
"2   5\n",
"1   3\n",
"3   9\n",
"3   3\n"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024Day1.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]
l1 = []
l2 = []

for i in game_data:
   vals = i.split()
   l1.append(vals[0])
   l2.append(vals[1])

print(l1)
print(l2)
part2(l1,l2)

l1.sort()
l2.sort()
part1(l1,l2)

