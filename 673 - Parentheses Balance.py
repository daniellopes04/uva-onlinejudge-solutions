def main():
    outputs = []

    cases = int(input())

    for _ in range(cases):
        line = input().strip()
        stack = []
        valid = True
        
        for char in line:
            if char in '[(':
                stack.append(char)

            elif char in '])':
                if len(stack) == 0:
                    valid = False
                    break

                topChar = stack.pop()

                if char == ']' and topChar != '[':
                    valid = False
                    break

                if char == ')' and topChar != '(':
                    valid = False
                    break
            else:
                valid = False

        valid = valid and len(stack) == 0

        outputs.append('{}'.format('Yes' if valid else 'No'))

    for item in outputs:
        print(item)

if __name__ == '__main__':
    main()