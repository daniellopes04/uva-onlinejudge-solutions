# -*- coding: UTF-8 -*-
def main():
    while True:
        try:
            k = int(input())

            x = k + 1
            y = (x * k) // (x - k)
            solutions = []

            while y > k and y >= x:    
                y, r = divmod(x * k, x - k)

                if r == 0:
                    solutions.append([x, y])
                x += 1

            print(len(solutions))

            for x, y in solutions:
                print('1/' + str(k) + ' = 1/' + str(y) + ' + 1/' + str(x))
                
        except(EOFError):
            break

if __name__=='__main__':
	main()
