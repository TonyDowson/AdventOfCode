import math

def map(game):
    directs = list()
    objs = set()
    for g in game:
        o = g.split(')')
        directs.append((o[0],o[1]))
        objs.add(o[0])
        objs.add(o[1])

    return directs,objs

def countPath(obj,orbits):
    #find obj
    orbitcount = 0
    for d in orbits:
        if (obj == d[1]):
            orbitcount = 1
            #print('Found it - ' + str(d[0]) + '->' + str(obj))
            #orbits.append((d[0],d[1]))
            orbitcount += countPath(d[0],orbits)

    return orbitcount
              

def countAllPaths(orbits,objs):
    #find obj
    orbitcount = 0
    for d in objs:
        print("Obj="+d)
        c = countPath(d,orbits)
        print('count ' + str(c))
        orbitcount += c

    return orbitcount        

#part 1 test data
test1 = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L'
        ]

game = test1
f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day6.txt", "r")
gd = f.readlines()
game = [i.strip('\n') for i in gd]

orbits,objs = map(game)
print("Orbits = " + str(orbits))
print("Objs = " + str(objs))

#count = countPath('D',orbits)
#print("total orbits = " + str(count))
#count = countPath('L',orbits)
#print("total orbits = " + str(count))
#count = countPath('COM',orbits)
#print("total orbits = " + str(count))

total = countAllPaths(orbits,objs)
print("total orbits = " + str(total))
