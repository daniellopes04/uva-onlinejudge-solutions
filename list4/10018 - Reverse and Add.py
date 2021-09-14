# -*- coding: UTF-8 -*-
def main():
	n = int(input())

	for _ in range(n):
		palindrome = int(input())
		iterations = 0

		while True:
			k = str(palindrome)

			if (k == k[::-1]):
				break
			else:
				m = int(k[::-1])
				palindrome += m
				iterations += 1
			
		print(iterations, palindrome)

if __name__ == '__main__':
    main()
