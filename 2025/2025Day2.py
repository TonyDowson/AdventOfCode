import math
import re

gd = [
"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
]

#gd = ["11-22,95-115"]

f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day2.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]
ranges = game_data[0].split(',')
total = 0

for i in ranges:
   vals = i.split('-')
   print(i)
   for n in range(int(vals[0]),int(vals[1]),1):
      s = str(n)
      l = len(s)
      if l % 2 == 0:
         s1 = s[0:int(l/2)]
         s2 = s[int(l/2):]
         #print(n)
         #print(s1 + "-" +s2)         
         if s1 == s2:
            total += n
             
print("Part 1 Total "+str(total))


def does_value_repeat(c,v):
   vals = re.split(c,v)
   good = True
   for i in vals:
      if len(i) > 0:
         good = False

   return good

total = 0
for i in ranges:
   vals = i.split('-')
   print(i)
   for n in range(int(vals[0]),int(vals[1])+1,1):
      s = str(n)

      for i in range(1,len(s)):
         if does_value_repeat(s[:i],s):
            print(s)
            total += n
            break

# 50847020260 is to high
# 50793864718
print("Part 2 Total "+str(total))
