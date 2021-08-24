# -*- coding: UTF-8 -*-
def pieces(n, k):
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
    numTests = int(input())
    solutionSpace = [1, 1, 2, 4]

    for _ in range(numTests):
        n = int(input())
        
        if n > 3:
            solution = 1
            solution += pieces(n, 2)
            solution += pieces(n, 4) 
        elif n >= 0:
            solution = solutionSpace[n]
        else:
            solution = 0
    
        print(int(solution))

if __name__ == '__main__':
    main()