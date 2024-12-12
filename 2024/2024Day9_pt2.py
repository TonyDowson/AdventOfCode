
	
gd = [
	'2333133121414131402'
]

f = open("Day9.txt", "r")
gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

fileid = chr(48)
converted = ""
convertedlist = []
count = 0
for i in gd[0]:
	if count % 2 == 1:
		converted += '.' * int(i)
		convertedlist.append('.' * int(i))
	else:
		converted += fileid * int(i)
		convertedlist.append(fileid * int(i))		
		fileid = chr(ord(fileid) + 1)
	count += 1

# reverse converted
reversedlist = [x for x in convertedlist[::-1] if x.find('.') == -1]
reversedlist = [x for x in reversedlist if x != '']
print(convertedlist)
print(reversedlist)

print("Moving...")
next = 0
newlist = []
for i in range(len(reversedlist)):
	l = len(reversedlist[i])
	if reversedlist[i].find('0') != -1:
		break
	for j in range(len(convertedlist)):
		if convertedlist[j].find('.') != -1:
			if len(convertedlist[j]) >= l:
				for k in range(len(convertedlist)):
					if reversedlist[i] == convertedlist[k]:
						if j < k:
							convertedlist[k] = ('.' * l)
						break
				if j<k:
					if len(convertedlist[j]) != l:
						dotstring = '.'*(len(convertedlist[j]) - l)
						convertedlist = convertedlist[0:j+1] + [dotstring] + convertedlist[j+1:]
					convertedlist[j] = reversedlist[i]					
				break

print(convertedlist)
new = ""
for x in convertedlist:
	new += x

checksum = 0
multiplier = 0
print(new)
#new = '00992111777.44.333....5555.6666.....8888..'
for i in new:
	if (i != '.'):
		checksum += (ord(i) - 48) * multiplier
	multiplier += 1

print("Total 1 " + str(checksum))

#  6408615561360 - too low
#  6415163624282
