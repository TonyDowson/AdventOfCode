# Function which returns subset or r length from n
from itertools import combinations
import re

def rSubset(arr, r):

    # return list of all subsets of length r
    # to deal with duplicate subsets use
    # set(list(combinations(arr, r)))
    return set(list(combinations(arr, r)))

# Driver Function
if __name__ == "__main__":
    arr = ["+", "*", "+", "*", "+", "*","+", "*", "+", "*", "+", "*"]
    r = 6
    #print (rSubset(arr, r))
    
    
def substring(string, letter='', substringList=[]):
    # Recursive function to create all the substrings
    #   of the given string

    if len(string) == 1:
        return substringList

    else:
        substringList.append(string[0]+letter+string[1])
        substring(string[1:], '*', substringList)
        substring(string[1:], '+', substringList)
        return substringList

#print(substring("bananas"))

def calc(vals,subtotal=0,results=[]):
	if len(vals) == 0:
		results.append(subtotal)
		return results
	else:
		if subtotal > 0:
			calc(vals[1:],subtotal*vals[0],results)
		calc(vals[1:],subtotal+vals[0],results)
		return results
		
#print(calc([19,10]))
l = ['5','4','3']
ln = [int(x) for x in l]
print(ln)
print(calc(ln))

'''
s = "| 'TOMATOES_PICKED'       |   914 |   1397 |"
pattern = re.compile(r"""\|\s*                 # opening bar and whitespace
                             '(?P<name>.*?)'       # quoted name
                             \s*\|\s*(?P<n1>.*?)   # whitespace, next bar, n1
                             \s*\|\s*(?P<n2>.*?)   # whitespace, next bar, n2
                             \s*\|""", re.VERBOSE)
match = pattern.match(s)
    
name = match.group("name")
n1 = float(match.group("n1"))
'''
s = "Button A: X+94, Y+34"
pattern = re.compile(r"""Button A: X\+\s*(?P<x>.*?), Y\+\s*(?P<y>.*?)""", re.VERBOSE)
match = pattern.match(s)
x = match.group("x")
y = match.group("y")
print(s)
print(x)
print(y)