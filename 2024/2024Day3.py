import re

def sum(s):
   total = 0
   muls = re.findall("mul\(\d+,\d+\)",s)

   for i in muls:
      x = re.findall("\d+",i)
      total += int(x[0]) * int(x[1])

   return total

gd = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
gd = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))do()"]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024Day3.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

total = sum(game_data[0])
print("Part 1 " + str(total))

g = re.sub("don\'t\(\).*?do\(\)","",game_data[0])
total = sum(g)
print("Part 2 " + str(total))