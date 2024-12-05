import math

def fuelRequired(mass):
    fuel = math.floor(mass / 3) -2 
    #print("mass="+str(mass)+" fuel="+str(fuel))    
    if (fuel > 8):
        fuel += fuelRequired(fuel)

    return fuel

gd = [
    "12\n",
    "14\n",
    "1969\n",
    "100756\n"
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day1.txt", "r")
gd = f.readlines()
total = 0
game_data = [i.strip('\n') for i in gd]

for m in game_data:
    fuel = fuelRequired(int(m))
    print(m+'='+str(fuel))    
    total += fuel

print("Total "+ str(total))