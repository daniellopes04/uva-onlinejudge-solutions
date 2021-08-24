# -*- coding: UTF-8 -*-
def rectangles(n, k):
    if k == n: 
        return 1

    if k > n: 
        return 0

    d = max(k, n - k)
    q = min(k, n - k)

    numerator =  1
    for n in range(d + 1, n + 1): 
        numerator *= n

    denominator = 1
    for d in range(1, q + 1): 
        denominator *= d

    return numerator // denominator

def main():
    cases = int(input())

    for _ in range(cases):
        line = input().split()
        numbers = list(map(int, line))

        n = numbers[0]
        k = numbers[1]

        stripes = sum(numbers[2:]) + k - 1
        
        print(rectangles(n - stripes + k, k))

if __name__ == '__main__':
    main()