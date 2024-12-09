def calc(vals,subtotal=0,results=[]):
	if len(vals) == 0:
		results.append(subtotal)
		return results
	else:
		if subtotal > 0:
			calc(vals[1:],subtotal*vals[0],results)
		calc(vals[1:],subtotal+vals[0],results)
		return results

def calc2(vals,subtotal=0,results=[]):
	if len(vals) == 0:
		results.append(subtotal)
		#return results
	else:
		if subtotal > 0:
			calc2(vals[1:],subtotal*vals[0],results)
			calc2(vals[1:],(int(str(subtotal)+str(vals[0]))),results)
		calc2(vals[1:],subtotal+vals[0],results)
		#return results

gd = [
   "190: 10 19\n",
   "3267: 81 40 27\n",
   "83: 17 5\n",
   "156: 15 6\n",
   "7290: 6 8 6 15\n",
   "161011: 16 10 13\n",
   "192: 17 8 14\n",
   "21037: 9 7 18 13\n",
   "292: 11 6 16 20"
]

f = open("Day7.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

sums = []
for g in game_data:
   sum = g.split(':')
   sums.append((int(sum[0]),[int(x) for x in sum[1].split()]))

print(sums)

total = 0
for s in sums:
	print(s)

	if s[0] in calc(s[1],0,[]):
		print('possible')
		total += s[0]

print("Total for Part 1 " + str(total))
print()
# 2299996598890 correct

total = 0
for s in sums:
	print(s)

	r = []
	calc2(s[1],0,r)
	if s[0] in r:
		print('possible')
		total += s[0]

print("Total for Part 2 " + str(total))
# 362646859298554 correct


