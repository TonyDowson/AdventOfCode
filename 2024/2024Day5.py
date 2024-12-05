import functools

gd = [
   "47|53\n",
   "97|13\n",
   "97|61\n",
   "97|47\n",
   "75|29\n",
   "61|13\n",
   "75|53\n",
   "29|13\n",
   "97|29\n",
   "53|29\n",
   "61|53\n",
   "97|53\n",
   "61|29\n",
   "47|13\n",
   "75|47\n",
   "97|75\n",
   "47|61\n",
   "75|61\n",
   "47|29\n",
   "75|13\n",
   "53|13\n",
   "75,47,61,53,29\n",
   "97,61,53,29,13\n",
   "75,29,13\n",
   "75,97,47,61,53\n",
   "61,13,29\n",
   "97,13,75,29,47",
]

f = open("C:\\Users\\U8001904\\OneDrive - London Stock Exchange Group\\Learning\\Python Learning\\AdventOfCode\\2024Day5.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

# Parse Page Ordering Rules and Page to product
y = 0
pageorderrules = {}
pagestoproduct = []
for g in game_data:
   rule = g.split('|')
   if len(rule) == 2:
      p = pageorderrules.get(rule[0])
      if p is None:
         pageorderrules[rule[0]] = [rule[1]]
      else:
         pageorderrules[rule[0]] = p + [rule[1]]
   else:
      pagestoproduct.append(g)

#print(pageorderrules)
#print(pagestoproduct)

# Part 1 - Old solution
total = 0
for m in pagestoproduct:
   pages = m.split(',')
   valid = True   
   for p in range(len(pages)-1):
      rule = pageorderrules.get(pages[p])
      #print(str(pages[p]) + "->" + str(rule))
      if rule is not None:
         for p2 in pages[p+1:]:
            if p2 not in rule:
               valid = False
               break
      else:
         valid = False
         break

   if valid:
      #print("Value to add " + pages[int((len(pages)-1) / 2)])
      total += int(pages[int((len(pages)-1) / 2)])      

print("Part 1 "+ str(total))


def compare(item1, item2):
   ret = 0  
   for i in pageorderrules.items():
      if item1 in i[1] and i[0] == item2:
         ret = 1
         break
      if item2 in i[1] and i[0] == item1:
         ret = -1
         break
   return ret

# Part 1 and 2
total1 = 0
total2 = 0
for m in pagestoproduct:
   l = m.split(',')
   #print(l)
   sortedlist = sorted(l, key=functools.cmp_to_key(compare)) 
   #print(sortedlist)
   if sortedlist != l:
      total2 += int(sortedlist[int((len(sortedlist)-1) / 2)])     
   else:
      total1 += int(sortedlist[int((len(sortedlist)-1) / 2)])  

print("Part 1 "+ str(total1))
print("Part 2 "+ str(total2))




  