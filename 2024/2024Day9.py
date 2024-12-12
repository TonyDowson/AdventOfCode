
	
gd = [
	'2333133121414131402'
]

f = open("Day9.txt", "r")
#gd = f.readlines()

game_data = [i.strip('\n') for i in gd]

fileid = chr(48)
converted = ""
count = 0
for i in gd[0]:
	if count % 2 == 1:
		converted += '.' * int(i)
	else:
		converted += fileid * int(i)
		fileid = chr(ord(fileid) + 1)
	count += 1

# reverse converted
reversed = [x for x in converted[::-1] if x != '.' ]
converted = [x for x in converted]
print(converted)
print(reversed)

next = 0
new = ""
for i in range(len(converted)):
	if converted[i] == '.':
		new += reversed[next]
		next += 1
	else:
		new += converted[i]

	if i + 2 > len(reversed):
		break

print(new)

checksum = 0
multiplier = 0
for i in new:
	checksum += (ord(i) - 48) * multiplier
	multiplier += 1

print("Total 1 " + str(checksum))

#  97218088249
#  10832401608155 - 2nd answer - fileid - too high
#  6385338159127 - correct
