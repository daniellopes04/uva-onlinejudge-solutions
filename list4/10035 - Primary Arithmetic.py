# -*- coding: UTF-8 -*-
def main():
    while True:
        line = input().split()
        n = line[0]
        m = line[1]

        if n == '0' and m == '0':
            break
        
        i = len(n) - 1
        j = len(m) - 1
        
        carryOuts = 0
        carry = 0

        while (i >= 0 or j >= 0):
            sum = 0

            if i >= 0:
                sum += carry + ord(n[i])
            else:
                sum += carry + ord('0')

            if j >= 0:
                sum += ord(m[j])
            else:
                sum += ord('0')
            
            sum -= 2*ord('0')

            if sum >= 10:
                carry = 1
                carryOuts += 1
            else:
                carry = 0

            i -= 1
            j -= 1
        
        if (carryOuts > 1):
            print(str(carryOuts) + ' carry operations.')
        elif (carryOuts == 1):
            print(str(carryOuts) + ' carry operation.')
        else:
            print('No carry operation.')

if __name__ == '__main__':
    main()