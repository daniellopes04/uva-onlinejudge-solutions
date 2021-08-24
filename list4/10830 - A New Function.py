# -*- coding: UTF-8 -*-
import math

def sumDivisors(x, n):
    return ((n * (n + 1) / 2) - (x * (x - 1) / 2))

def cumulativeSum(n):
    s = 0
    sum = long(s)
    sqrtN = (math.sqrt(n))

    for i in range(2, int(sqrtN+1)):
        limit = (n / i)
        sum += sumDivisors(i + 1, limit) + (i * (limit - i + 1))

    return sum

def main():
    cases = 1

    while True:
        try:
            n = int(input())

            print('Case ' + str(cases) + ': ' + str(cumulativeSum(n)))

            cases += 1
        except (EOFError) as e:
            break

if __name__ == '__main__':
    main()