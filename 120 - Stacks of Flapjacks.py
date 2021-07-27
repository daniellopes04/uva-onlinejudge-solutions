def main():
    while True:
        try:
            unsorted = list(map(int, input().split()))
            current = unsorted.copy()
            final = sorted(unsorted)

            N = len(final)
            steps = []

            for i in range(len(current) - 1, -1, -1):
                index  = current.index(final[i])
                
                if index == i:
                    continue

                if index == 0:
                    current[0:i + 1] = current[0:i + 1][::-1]
                    steps.append(N - i)
                else:
                    current[0:index + 1] = current[0:index + 1][::-1]
                    current[0:i + 1] = current[0:i + 1][::-1]

                    steps.append(N - index)
                    steps.append(N - i)

            steps.append(0)

            print(" ".join(map(str, unsorted)))
            print(" ".join(map(str, steps)))

        except(EOFError) as e:
            break

if __name__ == '__main__':
    main()