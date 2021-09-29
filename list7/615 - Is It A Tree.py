# -*- coding: UTF-8 -*-  
from collections import deque

buffer = []

def nextInt(n):
    global buffer

    while len(buffer) < n:
        line = input()
        
        if (line == ''):
            continue
        else:
            buffer += list(map(int, line.split()))

    next =  buffer[0:n]
    buffer = buffer[n:]

    return next

def main():
    inEdges = {}
    edges = {}
    vertices = set([])
    
    nEdges = 0
    case = 1
    hasLoop = False

    while True:
        u, v = nextInt(2)

        if (u < 0):
            break

        if (u == 0 and v == 0):
            if (len(vertices) == 0):
                response = "a tree"
            elif (hasLoop or len(vertices) != nEdges + 1):
                response = "not a tree"
            else:
                zeroDegree = 0
                root = -1
                for v in vertices:
                    if (not v in inEdges):
                        zeroDegree += 1
                        root = v

                if (zeroDegree != 1):
                    response = "not a tree"
                else:
                    reached = set()
                    reached.add(root)
                    q = deque([root])

                    while len(q) > 0:
                        c = q.pop()

                        if (c in edges):
                            for edge in edges[c]:
                                if (not edge in reached):
                                    reached.add(edge)
                                    q.append(edge)

                if (len(reached) == len(vertices)):  
                    response = "a tree"
                else:
                    response = "not a tree"

            print('Case ' + str(case) + ' is ' + response + '.')

            vertices.clear()
            inEdges.clear()
            edges.clear()

            nEdges = 0
            case += 1
            hasLoop = False
        else:
            vertices.add(u)
            vertices.add(v)

            if (u == v):
                hasLoop = True
                continue

            nEdges += 1

            if (not v in inEdges):
                inEdges[v] = 1
            else:
                inEdges[v] += 1

            if (not u in edges):
                edges[u] = [v]
            else:
                edges[u].append(v)

if __name__=='__main__':
	main()