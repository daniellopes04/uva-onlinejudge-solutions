# -*- coding: UTF-8 -*-
import math

def main():
    while True:
        try:
            line = input().split()
            n = int(line[0])
            k = int(line[1])

            digits = 0

            if (k > n - k):
                for i in range(k + 1, n + 1):
                    digits += (math.log10 (i) - math.log10 (n - i + 1))
            else:
                for i in range(n - k + 1, n + 1):
                    digits += (math.log10 (i) - math.log10 (n - i + 1))
            
            print(math.floor(digits)+1)

        except(EOFError):
            break

if __name__ == '__main__':
    main()