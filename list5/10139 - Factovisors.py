# -*- coding: UTF-8 -*-
import collections 

def primeFactors(n):
    i = 2
    factors = []

    while i * i <= n:
        if (n % i):
            i += 1
        else:
            n //= i
            factors.append(i)
    
    if (n > 1):
        factors.append(n)

    return factors

def main():
    while True:
        try:
            line = input().split()
            n = int(line[0])
            m = int(line[1])

            factors = collections.Counter(primeFactors(m))
            
            divides = True
            for prime, frequency in factors.items():
                tempFrequency = 0
                temp = prime

                while n >= temp:
                    tempFrequency += n // temp
                    temp = temp * prime
                
                if tempFrequency < frequency:
                    divides = False
                    break

            if divides:
                print(str(m) + ' divides ' + str(n) + '!')
            else:
                print(str(m) + ' does not divide ' + str(n) + '!')
                
        except(EOFError):
            break

if __name__ == '__main__':
    main()