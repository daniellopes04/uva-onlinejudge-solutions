# -*- coding: UTF-8 -*-
def isPrime(n):
    for a in range(2, n):
        if (not pow(a, n, n) == a):
            return False
    
    return True

def sievePrimes(n):
    size = n // 2
    sieve = [1] * size
    limit = int(n ** 0.5)

    for i in range(1, limit):
        if (sieve[i]):
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val 
            sieve[i + val::val] = [0] * tmp

    return [2] + [i * 2 + 1 for i, v in enumerate(sieve) if v and i > 0]

def main():
    primes = set(sievePrimes(65000))

    while True:
        number = int(input())

        if (number == 0):
            break
        
        if ((not number in primes) and (isPrime(number))):
            print('The number ' + str(number) + ' is a Carmichael number.')
        else:
            print(str(number) + ' is normal.')

if __name__ == '__main__':
    main()