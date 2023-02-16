def allPermut():
    s = input().split()
    for i in range(len(s)):
        for j in range(len(s)-1):
            print(*s)
            s[j], s[j+1] = s[j+1], s[j]
allPermut()





#2
"""
from itertools import permutations

def permutation(str):
	perm = sorted(''.join(chars) for chars in permutations(str))
	for x in perm:
		print(x)
		
str = input()
permutation(str)
"""
