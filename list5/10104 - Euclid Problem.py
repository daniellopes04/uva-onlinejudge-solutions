# -*- coding: UTF-8 -*-
import math

x, y, d = 0, 0, 0

def euclid(a, b):
    global x, y, d

    if (b == 0):
        x = 1
        y = 0
        d = a
        return
    
    euclid(b, a % b)

    tempX = y
    tempY = x - math.floor(a / b) * y

    x = tempX
    y = tempY

def main():
    while True:
        try:
            line = input().split()
            a = int(line[0])
            b = int(line[1])

            if (a == 0):
                 a, b = b, a

            euclid(a, b)
            print(str(x) + ' ' + str(y) + ' ' + str(d))
                
        except(EOFError):
            break

if __name__ == '__main__':
    main()