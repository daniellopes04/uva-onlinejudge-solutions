# -*- coding: UTF-8 -*-
from math import sqrt

def main():
    while True:
        try:
            num = int(input())

            if (num == 0):
                break

            div = sqrt(num)

            if (div == int(div)):
                print('yes')
            else:
                print('no')
                
        except(EOFError):
            break

if __name__ == '__main__':
    main()