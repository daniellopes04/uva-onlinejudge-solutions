# -*- coding: UTF-8 -*-
def main():
    while True:
        try:
            line = input().strip()
            
            while line == "":
                line = input().strip()
            
            items = line.split()

            if len(items) == 2:
                n = int(items[0])
                text = items[1]
            else:
                n = int(items[0])
                text = input().strip()
                while text == "":
                    text = input().strip()

            frequency = {}

            for i in range(len(text) - n + 1):
                substr = text[i:i+n]

                if substr in frequency:
                    frequency[substr] += 1
                else:
                    frequency[substr] = 1

            password = max(frequency.keys(), key=(lambda k: frequency[k]))
            print(password)

        except(EOFError):
            break

if __name__ == '__main__':
    main()