import math

gd = [
"L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"
]

f = open("C:\\Users\\tdowson\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2025\\2025Day1.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]
dial = 50
total = 0

for i in game_data:
   print(i)
   v = (int(i[1:]) % 100)
   if (i[0] == 'L'):
      dial -= v
      if (dial < 0):
         dial += 100
   else:
      dial += v 
      if (dial > 99):
         dial -= 100
   print(dial)         
   if (dial == 0):
      total += 1 

print("Dial "+str(dial))
print("Part 1 Total "+str(total))

#Part 2
print("\n\nPart 2")
dial = 50
previous = 50
total = 0

for i in game_data:
   print("\n" + i)
   val = int(i[1:])
   v = val % 100
   if val > 99:
      total += math.floor(int(val / 100))
   previous = dial

   if (i[0] == 'L'):
      dial -= v                      
   else:
      dial += v      

   if (dial < 0):
      dial += 100
      if (not previous == 0):
         total += 1  
   elif (dial > 99):        
      dial -= 100
      if (not previous == 0):         
         total += 1
   elif (dial == 0):
      total += 1           
   
   if (val > 99):
      print("************************")
   print("Dial " + str(dial))          
   print("Total " + str(total))         

#6977 is too high
#5933

print("\nDial "+str(dial))
print("Part 2 Total "+str(total))