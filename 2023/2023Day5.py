
def buildDictionary(f):
    line = f.readline()
    map = []
    while (line and line != '\n'):
        m = line.split()
        map.append((int(m[0]),int(m[1]), int(m[2])))
        line = f.readline()    
    print(map)  
    return map

def lookup(map,value):
    v = value
    for m in map:
        if (value >= m[1] and value <= (m[1]+ m[2])):
            v = (m[0]-m[1]) + value
            break
    return v
    

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2023Day5.txt", "r")
minLocation = 0
x = f.readline()

while x:
    print(x)
    if (x.find("seeds:") != -1):
        seeds = x[6:].split()
    elif (x.find("seed-to-soil map:") != -1):
        seedtoSoil = buildDictionary(f)
    elif (x.find("soil-to-fertilizer map:") != -1):
        soilToFert = buildDictionary(f)
    elif (x.find("fertilizer-to-water map:") != -1):
        fertToWater = buildDictionary(f)
    elif (x.find("water-to-light map:") != -1):
        waterToLight = buildDictionary(f)            
    elif (x.find("light-to-temperature map:") != -1):
        lightToTemp = buildDictionary(f)      
    elif (x.find("temperature-to-humidity map:") != -1):
        tempToHumid = buildDictionary(f)   
    elif (x.find("humidity-to-location map:") != -1):
        humidToLocation = buildDictionary(f)
    x = f.readline()

#create a list of dictionaries ??

loc = 0
for x in seeds:
    s = lookup(seedtoSoil,int(x))
    f = lookup(soilToFert,s)     
    w = lookup(fertToWater,f)     
    l = lookup(waterToLight,w)
    t = lookup(lightToTemp,l)       
    h = lookup(tempToHumid,t)        
    l = lookup(humidToLocation,h)
    print("Seed="+x+" Soil="+str(s) + " Fert="+str(f)+ " Water="+str(w))      

    if (loc == 0):
        loc = l
    elif (l < loc):
        loc = l

print ("Answer is")
print(loc)
