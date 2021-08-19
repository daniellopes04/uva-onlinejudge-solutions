# -*- coding: UTF-8 -*-
def main():
    while True:
        line = input().split()

        n = int(line[0])
        m = int(line[1])

        if n == 0 and m == 0:
            break

        order = []
        inEdges = [(i, []) for i in range(n)]

        for i in range(0, m):
            line = input().split()

            fromTask = int(line[0]) - 1
            toTask = int(line[1]) - 1

            if not fromTask in inEdges[toTask][1]:
                inEdges[toTask][1].append(fromTask)

        while len(inEdges) > 0:
            target = -1
            for i in range(len(inEdges)):
                if len(inEdges[i][1]) == 0:
                    target = i
                    order.append(inEdges[i][0] + 1)
                    break
            
            if target >= 0:
                id = inEdges[target][0]
                inEdges.remove(inEdges[target])
            
                for i in range(len(inEdges)):
                    if id in inEdges[i][1]:
                        inEdges[i][1].remove(id)
        
        print(' '.join(map(str, order)))

if __name__ == '__main__':
    main()