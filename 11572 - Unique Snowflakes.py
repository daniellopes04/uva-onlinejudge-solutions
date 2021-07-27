def main():
    n = int(input().strip())

    for _ in range(0, n):
        itemsNumber = int(input().strip())
    
        numbers = [] 
        dic = {}
        currSequence = 0
        maxSequence = 0

        for i in range(itemsNumber):
            item = int(input().strip())
            numbers.append(item)

            if item in dic:
                if currSequence > maxSequence:
                    maxSequence = currSequence

                old_val = dic[item]

                for v in range(i - currSequence, old_val+1):
                    del dic[numbers[v]]
                    currSequence -= 1

                dic[item] = i
                currSequence += 1

            else:
                currSequence += 1
                dic[item] = i
        
        if currSequence > maxSequence:
            maxSequence = currSequence

        print(maxSequence)

if __name__ == '__main__':
    main()