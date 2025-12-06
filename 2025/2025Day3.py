import math
import re

gd = [
"987654321111111",
"811111111111119",
"234234234234278",
"818181911112111",
]

f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day3.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]
total = 0

def find_largest(pos,i,n):
   max = 0
   pos1 = 0
   for j in range(pos,len(i)-n):
      if int(i[j]) > max:
         max = int(i[j])   
         pos1 = j
   return max,pos1

for i in game_data:
   print(i)
   first_max,pos1 = find_largest(0,i,1)
   second_max,pos2 = find_largest(pos1+1,i,0)

   '''
   for j in range(0,len(i)-1):
      if int(i[j]) > first_max:
         first_max = int(i[j])
         pos = j
        
   for j in range(pos+1,len(i)):
      if int(i[j]) > second_max:
         second_max = int(i[j])
   '''
   print("1st max " + str(first_max) + "  2nd max " + str(second_max))
   total += (first_max * 10) + second_max     
print("Part 1 Total "+str(total))



total = 0
for i in game_data:
   pos = 0   
   tot = ""
   print(i)
   for j in range(12,0,-1):
      max, pos = find_largest(pos,i,j-1)
      pos += 1
      tot = tot + str(max)

   print("Sub Total " +tot)
   total += int(tot)
   
print("Part 2 Total "+str(total))




