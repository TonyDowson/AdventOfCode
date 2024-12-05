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

def countPath(obj,orbits,path):
    #find obj
    for d in orbits:
        if (obj == d[1]):
            orbitcount = 1
            #print('Found it - ' + str(d[0]) + '->' + str(obj))
            path.append(d[0])
            return countPath(d[0],orbits,path)

    return path
              

def countAllPaths(orbits,objs):
    #find obj
    orbitcount = 0
    for d in objs:
        #print("Obj="+d)
        path = countPath(d,orbits,list())
        #print('path=' + str(path) + ' count=' + str(len(path)))
        orbitcount += len(path)

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

#f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day6.txt", "r")
#gd = f.readlines()
#game = [i.strip('\n') for i in gd]

orbits,objs = map(game)
print("Orbits = " + str(orbits))
print("Objs = " + str(objs))

path = countPath('D',orbits,list())
print('path = ' + str(path) + ' total orbits = ' + str(len(path)))
path = countPath('L',orbits,list())
print('path = ' + str(path) + ' total orbits = ' + str(len(path)))
path = countPath('COM',orbits,list())
print('path = ' + str(path) + ' total orbits = ' + str(len(path)))

total = countAllPaths(orbits,objs)
print("total orbits = " + str(total))
