# -*- coding: UTF-8 -*-
import math

def checkIsPrime(num):
	s = int(math.sqrt(num))

	for i in range(2, s + 1):
		if (num % i == 0):
			return False

	return True

def getPrimes(num):
    primes = [0, 0]
    for i in range(2, int(num / 2) + 1):
        if (checkIsPrime(i) and checkIsPrime(num - i)):
            primes[0] = i
            primes[1] = num - i

            return primes

def main():
    while True:
        try:
            n = int(input())

            if(n <= 7):
                print("Impossible.")

            if (n % 2 != 0):
                primes = getPrimes(n - 5)
                
                if (primes):
                    print("2 3", primes[0], primes[1])
            else:
                primes = getPrimes(n - 4)

                if (primes):
                    print("2 2", primes[0], primes[1])
                
        except(EOFError):
            break

if __name__=='__main__':
	main()
