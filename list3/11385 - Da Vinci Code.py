# -*- coding: UTF-8 -*-
def main():
    fibonacci = {}
    LIMIT = 100

    fibList = [1,2]
    for _ in range(0, LIMIT + 1):
        fibList.append(fibList[-1] + fibList[-2])

    for i in range(0, LIMIT + 1):
        fibonacci[fibList[i]] = i


    cases = int(input())

    for _ in range(cases):
        n = input()
    
        code = []
        line = input().split()

        for i in range(0, int(n)):
            code.append(int(line[i]))

        cipher = input().strip()

        decoded = [' '] * LIMIT
        i = 0
        strSize = 0

        for c in cipher:
            if i >= len(code):
                break
            if c.isupper():
                index = fibonacci[code[i]] 
                decoded[index] = c
                strSize = max(strSize, index+1)
                i += 1
                
        print("".join(decoded[:strSize]))

if __name__ == '__main__':
    main()