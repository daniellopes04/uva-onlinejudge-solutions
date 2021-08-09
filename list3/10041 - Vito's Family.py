# -*- coding: UTF-8 -*-
import math

def main():
    cases = int(input())

    for i in range(0, cases):
        numbers = []

        for x in input().split():
            numbers.append(int(x))

        count = numbers[0]

        locations = sorted(numbers[1:])
        medianIndex = math.floor(count / 2)
        distance = 0 

        times = 1

        for i in range(1, medianIndex+1):
            distance += times * (locations[i] - locations[i-1])
            times += 1 
        
        times = 1
        
        for i in range(count - 1, medianIndex, -1):
            distance += times * (locations[i] - locations[i-1])
            times += 1 
        
        print(distance)

if __name__ == '__main__':
    main()