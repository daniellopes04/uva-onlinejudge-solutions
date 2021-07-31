# -*- coding: UTF-8 -*-
def main():
	while True:
		l = input().split()
		n = int(l[0])
		k = int(l[1])

		if n == 0 and k == 0:
			break

		for j in range(1, n+1):
			pos = j
			circle = [i for i in range(0, n+1)]

			counter = 0
			last = [-1, -1]
			kill = True
			temp = 0

			while (counter < n):
				if (circle[pos] > 0):
					temp += 1
				
				if (temp == k and circle[pos] > 0):
					if (kill):
						last[0] = pos
						last[1] = circle[pos]
						circle[pos] = -1
						kill = False
						counter += 1
					else:
						circle[last[0]] = circle[pos]
						last[1] = circle[pos]
						circle[pos] = -1
						pos = last[0]
						kill = True
					
					temp = 0
				pos += 1
				
				if (pos > n):
					pos = 1
			
			if (last[1] == 1):
				res = j
				break
		
		print(res)

if __name__ == '__main__':
    main()