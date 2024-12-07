def setWorkflow(workflows):

    allworkflows = {}
    for w in workflows:
       flow = w.split('{')
       allworkflows[flow[0]] = flow[1].split(',')

    print(allworkflows)
    return allworkflows

def extractPartValue(pv, parts):
    p = parts.split(',')
    for i in p:
        v = i.split('=')
        if (pv == v[0]):
            return int(v[1])
    return 0
      

def sumParts(parts):
   return 1

def checkCondition(cond,parts):
    print("Condition to evaluate "+cond)
    if '>' in cond:
        c = cond.split('>')
        if (extractPartValue(c[0],parts) > int(c[1])):
            return True
    elif '<' in cond:
        c = cond.split('<')
        if (extractPartValue(c[0],parts) < int(c[1])):
            return True   
        
    return False

def applyWorkflow(workflows, parts, pos):
    print("Part="+parts)
    if pos == "A":
        return sumParts(parts)
    elif pos == 'R':
        return 0       
    w = workflows[pos]
    for i in w:
        if '>' in i:
           print(">  " + i)
           if checkCondition(i.split(':')[0],parts):
                return applyWorkflow(workflows, parts, i.split(':')[1])
        elif '<' in i:
           print("<  " + i)
           if checkCondition(i.split(':')[0],parts):
                return applyWorkflow(workflows, parts, i.split(':')[1])       
        elif 'A' in i:
            print("A  " + i)
            return sumParts(parts)
        elif 'R' in i:
           print("R  " + i) 
           return 0               
        else:
           print("go to "+i)
           return applyWorkflow(workflows, parts, i)

    return 0


game_data = [
    "px{a<2006:qkq,m>2090:A,rfg}\n",
    "pv{a>1716:R,A}\n",
    "lnx{m>1548:A,A}\n",
    "rfg{s<537:gd,x>2440:R,A}\n",
    "qs{s>3448:A,lnx}\n",
    "qkq{x<1416:A,crn}\n",
    "crn{x>2662:A,R}\n",
    "in{s<1351:px,qqz}\n",
    "qqz{s>2770:qs,m<1801:hdj,R}\n",
    "gd{a>3333:R,R}\n",
    "hdj{m>838:A,pv}\n",
    "\n",
    "{x=787,m=2655,a=1222,s=2876}\n",
    "{x=1679,m=44,a=2067,s=496}\n",
    "{x=2036,m=264,a=79,s=2244}\n",
    "{x=2461,m=1339,a=466,s=291}\n",
    "{x=2127,m=1623,a=2188,s=1013}\n"
]


#f = open("C:\\Users\\t_dow\\Documents\\GitHub\\Python\\2023Day19.txt", "r")
#f = open("2023Day19.txt", "r")
#game_data = f.readlines()

workflows = []
first = True
total = 0
for g in game_data:
    if g == '\n':
       workflows = setWorkflow(workflows)
       first = False
       continue

    if first:
       workflows.append(g.strip('}\n'))
    else:
        break

for x in range(4000):
    print("x " + str(x))
    for m in range(1):
        for a in range(1):
            for s in range(1):
                p = "x="+str(x)+",m="+str(m)+",a="+str(a)+",s="+str(s)
                total += applyWorkflow(workflows,p,"in")

print("sum is " +str(total))
      
      

