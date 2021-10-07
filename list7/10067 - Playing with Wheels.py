# -*- coding: UTF-8 -*-  
from collections import deque

class Graph:
    def __init__(self):
        NUM_VERTICES = 10000

        self.numVertices = NUM_VERTICES
        self.edges = [[] for _ in range(self.numVertices)]
        self.forbiddenStates = set([])

        def __setData():
            def toInt(a, b, c, d):
                return d + c * 10 + b * 100 + a * 1000

            for i in range(self.numVertices):
                t = i
                t, d = divmod(t, 10)
                t, c = divmod(t, 10)
                a, b = divmod(t, 10)
                
                self.edges[i] = [
                    toInt(a, b, c, d - 1 if d > 0 else 9),
                    toInt(a, b, c, d + 1 if d < 9 else 0),
                    toInt(a, b, c - 1 if c > 0 else 9, d),
                    toInt(a, b, c + 1 if c < 9 else 0, d),
                    toInt(a, b - 1 if b > 0 else 9, c, d),
                    toInt(a, b + 1 if b < 9 else 0, c, d),
                    toInt(a - 1 if a > 0 else 9, b, c, d),
                    toInt(a + 1 if a < 9 else 0, b, c, d),
                ]

        __setData()

    def setForbiddenStates(self, forbiddenConf):
        self.forbiddenStates = set(forbiddenConf)

    def validEdge(self, verticeStart, verticeEnd):
        if verticeEnd  in self.forbiddenStates:
            return False

        return True 

    def minPath(self, initial, target):
        if initial == target:
            return 0

        distanceFromInitial = [-1] * self.numVertices

        def calculateMinPath(start, end):
            discovered = [False] * self.numVertices

            q = deque([start])
            distanceFromInitial[start] = 0
            discovered[start] = True

            while len(q) > 0:
                v = q.popleft()
                
                for y in self.edges[v]:
                    if not self.validEdge(v, y):
                        continue

                    if not discovered[y]:
                    
                        discovered[y] = True
                        distanceFromInitial[y] = distanceFromInitial[v] + 1 

                        if y == end:
                            return

                        q.append(y)
            
            return 

        calculateMinPath(initial, target)
        return distanceFromInitial[target]

def toInt(a, b, c, d):
    return d + c * 10 + b * 100 + a * 1000

def main():
    cases = int(input())
    graph = Graph()

    for _ in range(cases):
        line = input().strip()

        while line == "":
            line = input().strip()
        
        initialConf = toInt(*list(map(int, line.split())))
        targetConf = toInt(*list(map(int, input().split())))

        forbiddenConf = []
        nForbiddenConf = int(input())
        
        for _ in range(nForbiddenConf):
            forbiddenConf.append(toInt(*list(map(int, input().split()))))

        graph.setForbiddenStates(forbiddenConf)

        print(graph.minPath(initialConf, targetConf))

if __name__=='__main__':
	main()