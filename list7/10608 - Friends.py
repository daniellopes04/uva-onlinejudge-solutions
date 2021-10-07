# -*- coding: UTF-8 -*-  
MAX = 30001
citizens = [0 for _ in range(MAX)]
pairs = [0 for _ in range(MAX)]

def init(n):
	global citizens, pairs

	for i in range(n + 1):
		pairs[i] = i
		citizens[i] = 1

def findPair(x):
	global pairs

	if (pairs[x] != x):
		pairs[x] = findPair(pairs[x])
	
	return pairs[x]

def link(x, y):
	global citizens, pairs

	if (citizens[x] > citizens[y]):
		citizens[x] += citizens[y]
		pairs[y] = x
	else:
		citizens[y] += citizens[x]
		pairs[x] = y

def union(x, y):
	x = findPair(x)
	y = findPair(y)

	if (x != y):
		link(x, y)

def main():
	global pairs

	cases = int(input())

	for _ in range(cases):
		line = input().split()
		nCitizens, nPairs = int(line[0]), int(line[1])

		init(nCitizens)

		for _ in range(nPairs):
			line = input().split()
			personA, personB = int(line[0]), int(line[1])

			union(personA, personB)
		
		max = 0
		for i in range(nCitizens + 1):
			if (citizens[i] > max):
				max = citizens[i]

		print(max)

if __name__=='__main__':
	main()