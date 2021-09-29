# -*- coding: UTF-8 -*-
n, m = 0, 0
i, j = 0, 0
result, sum = 0, 0
map, used = [], []
land = ''

def find(x, y):
    global n, m, i, j, result, sum, map, used, land

    if (y < 0):
        y = n - 1
    
    if (y >= n):
        y = 0
    
    if (x < 0 or x >= m):
        return
    
    if (used[x][y] != 0 or map[x][y] != land):
        return
    
    used[x][y] = 1
    sum += 1

    find(x + 1, y)
    find(x, y + 1)
    find(x - 1, y)
    find(x, y - 1)


def main():
    global n, m, i, j, result, sum, map, used, land

    while True:
        try:
            line = input().split()
            m = int(line[0])
            n = int(line[1])

            map = []
            used = []

            for i in range(m):
                mapLine = input().strip()
                auxList = []
                auxListUsed = []

                for j in range(n):
                    auxList.append(mapLine[j])
                    auxListUsed.append(0)

                map.append(auxList)
                used.append(auxListUsed)
            
            line = input().split()
            i = int(line[0])
            j = int(line[1])

            land = map[i][j]

            find(i, j)
            result = 0

            for k in range(m):
                for l in range(n):
                    sum = 0
                    find(k, l)

                    if (sum > result):
                        result = sum
            
            print(result)
            _ = input()

        except(EOFError):
            break


if __name__=='__main__':
	main()

