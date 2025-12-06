import math
import re

gd = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  ",
]

f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day6.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]
numbers = {}
signs = {}
x = 0
y = 0

for g in game_data:
   vals = g.split(' ')
   print(vals)
   x = 0
   for v in vals:
      if v == '':
         continue
      if v.isnumeric():
         numbers[(x,y)] = int(v)
      else:
         signs[(x,0)] = v
      x += 1
   y += 1

maxx = x
maxy = y-1
print(numbers)
print(signs)

total = 0
for i in range(0,maxx):
   sub = numbers[(i,0)]
   s = signs[(i,0)]   
   for j in range(1,maxy):
      n = numbers[(i,j)]
      if s == '*':
         sub *= n
      else:
         sub += n
   print("Sub="+str(sub))
   total += sub
print("Total= " +str(total))




matrix = []
for g in game_data:
   print(g)
   matrix.append(g+' ')

total = 0
sinc = 0
maxx = len(matrix[0])
nums = []
print("Maxx= "+ str(maxx))
print("Maxy= "+ str(maxy))
print(matrix)
for i in range(0,maxx):
   n = ""
   for j in range(0,maxy):
      m = matrix[j][i]

      if m.isnumeric():
         n = n + m

   if n == '':
      print("Calculate")      
      print(nums)
      print(signs[(sinc,0)])
      if signs[(sinc,0)] == '+':
         sub = 0
         for x in nums:
            sub += x
      else:
         sub = 1
         for x in nums:
            sub *= x         
      print("Sub= "+str(sub))
      total += sub
      nums = []
      sinc += 1
   else:
      nums.append(int(n))
      print("Number is " + n)
      
print("Total= " +str(total))