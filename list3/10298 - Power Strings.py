# -*- coding: UTF-8 -*-
import math

def generate(n):
    largeDivisors = []

    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
        
            if i*i != n:
                largeDivisors.append(math.floor(n / i))

    for divisor in reversed(largeDivisors):
        yield divisor

def main():
    string = str(input())

    while string != ".":
        for divisor in generate(len(string)):
            power = math.floor(len(string) / divisor)
            found = True

            for i in range(power):
                if string[0:divisor] != string[i*divisor:i*divisor+divisor]:
                    found = False
                    break

            if found:
                break
        
        print(power)
        string = str(input())

if __name__ == '__main__':
    main()