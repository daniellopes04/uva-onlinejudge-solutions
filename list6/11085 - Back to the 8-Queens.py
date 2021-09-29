# -*- coding: UTF-8 -*-  
queens = []
path = []

def isValid(r, c):
    global queen, path

    for j in range(r):
        if (c == path[j]):
            return False
        
        if (abs(r - j) == abs(c - path[j])):
            return False
    
    return True

def search(n):
    global queen, path
    total = 100000

    if (n == 8):
        return 0
    
    for i in range(8):
        if isValid(n, i):
            path[n] = i

            total = min(total, search(n + 1) if i == queens[n] else 1 + search(n + 1))

    return total


def main():
    global queens, path
    count = 1

    while True:
        try:
            line = input().split()

            queens = []
            path = []

            for item in line:
                queens.append(int(item) - 1)
                path.append(int(item))

            print('Case ' + str(count) + ': ' + str(search(0)))

            count += 1

            
        except(EOFError):
            break
        
if __name__=='__main__':
	main()
