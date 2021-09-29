# -*- coding: UTF-8 -*-
def calculateBest(s, d):
    maxPositive = 5

    while maxPositive > 0 and s * maxPositive - d * (5 - maxPositive) >= 0:
        maxPositive -= 1

    minNegative = 5 - maxPositive
    
    if (maxPositive == 0):
        return -1
    
    sumResult = 0
    position = 0

    while position < 12:
        positiveN = min(12 - position, maxPositive)
        sumResult += positiveN * s
        position += positiveN

        negativeN = min(12 - position, minNegative)
        sumResult -= negativeN * d
        position += negativeN

    return sumResult

def main():
    while True:
        try:
            line = input().split()
            s = int(line[0].strip())
            d = int(line[1].strip())

            surplus = calculateBest(s, d)

            if (surplus > 0):
                print(surplus)
            else:
                print('Deficit')
                
        except(EOFError):
            break

if __name__=='__main__':
	main()
