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

def getDistBtPaths(path1, path2):
    found = False
    count = 0
    for p1 in path1:
        #print('p1 '+str(p1))
        for p2 in path2:
            #print('p2 '+str(p2))
            if (p1 == p2):
                found = True
                count += 1
                break
        if not found:
            break
    
    return (len(path1) + len(path2) - (2 * count))
        
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

test2 = [
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
        'K)L',
        'K)YOU',
        'I)SAN'
        ]


f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\2019Day6.txt", "r")
gd = f.readlines()
game = [i.strip('\n') for i in gd]

# part 1 - test
orbits,objs = map(test1)
print("Test1 Orbits = " + str(orbits))
print("Test1 Objs = " + str(objs))
total = countAllPaths(orbits,objs)
print("total orbits = " + str(total))
# part 1 - real
orbits,objs = map(game)
total = countAllPaths(orbits,objs)
print("full input - total orbits = " + str(total))


#part 2
orbits,objs = map(test2)
path1 = countPath('YOU',orbits,list())
print('Test2 path = ' + str(path1) + ' total orbits = ' + str(len(path1)))
path2 = countPath('SAN',orbits,list())
print('Test2 path = ' + str(path2) + ' total orbits = ' + str(len(path2)))
print('Test2 dist = ' + str(getDistBtPaths(path1[::-1], path2[::-1])))

# part 2 - real
orbits,objs = map(game)
path1 = countPath('YOU',orbits,list())
#print('Test2 path = ' + str(path1) + ' total orbits = ' + str(len(path1)))
path2 = countPath('SAN',orbits,list())
#print('Test2 path = ' + str(path2) + ' total orbits = ' + str(len(path2)))
print('Full input dist = ' + str(getDistBtPaths(path1[::-1], path2[::-1])))


