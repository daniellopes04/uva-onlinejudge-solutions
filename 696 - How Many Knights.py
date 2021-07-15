def solve(n, m):
    if (n > m):
        n, m = m, n

    if (n == 1):
        return m
    if (n == 2):
        ans = int((m / 4)) * 4

        if ((m % 4) == 0):
            return ans
        else:
            if((m % 4) > 1):
                return ans + 4
            else:
                return ans + 2
    
    return int((n * m + 1) / 2)

def main():
    outputs = []

    while True:
        string = input()
        string.strip()

        if string == '0 0':
            break
        
        n, m = string.split()
        n = int(n)
        m = int(m)

        outputs.append(str(solve(n, m)) + ' knights may be placed on a ' + str(n) +' row ' + str(m) +' column board.')

    for line in outputs:
        print(line)

if __name__ == '__main__':
    main()