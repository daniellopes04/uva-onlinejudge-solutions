# -*- coding: UTF-8 -*-
def main():
    while True:
        line = input().strip()

        if line == '0': 
            break
        
        n = int(line)
        ordered = [i + 1 for i in range(0, n)]

        line = input().strip()

        while (line != '0'):
            unordered = list(map(int, line.split()))
            possible = True

            stack = []
            inIndex = 0
            outIndex = 0

            while (outIndex < n):
                if (inIndex < n and ordered[inIndex] == unordered[outIndex]):
                    inIndex += 1
                    outIndex += 1
                elif (len(stack) > 0 and stack[-1] == unordered[outIndex]):
                    stack.pop()
                    outIndex += 1
                else:
                    if (inIndex < n):
                        stack.append(ordered[inIndex])
                        inIndex += 1
                    else:
                        possible = False
                        break

            print('Yes\n' if possible else 'No\n', end='')
            
            line = input().strip()

        print('')

if __name__ == '__main__':
    main()