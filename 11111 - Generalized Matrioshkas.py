# -*- coding: UTF-8 -*-
def main():
    try:
        while True:
            line = input().strip().split()
            
            stack1 = list()
            stack2 = list()
            i = 0
            j = len(line)
            band = True
            s = None
            
            while (band and i < j):
                toy = int(line[i])

                if toy < 0:
                    stack1.append(toy)
                    stack2.append(toy*(-1))

                else:
                    if (len(stack1) == 0 or stack1[-1] + toy != 0):
                        band = False

                    else:
                        stack2.pop()
                        stack1.pop()
                        
                        if (len(stack1) > 0):
                            s = stack2.pop() - toy
                            
                            if s <= 0:
                                band = False

                            stack2.append(s)
                i += 1

            band = band and len(stack1) == 0

            if band:
                print(':-) Matrioshka!')
            
            else:
                print(':-( Try again.')
    
    except(EOFError):
        pass

if __name__ == '__main__':
    main()