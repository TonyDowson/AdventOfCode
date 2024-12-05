import math

def fuelRequired(mass):
    fuel = math.floor(int(mass) / 3) -2 
    print("mass="+mass+" fuel="+str(fuel))
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
    total += fuelRequired(m)

print("Total "+ str(total))