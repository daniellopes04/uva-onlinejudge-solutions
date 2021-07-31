# -*- coding: UTF-8 -*-
def main():
    reverses = {
        'A': 'A', 'B': '', 'C': '', 'D': '', 'E': '3', 
        'F': '', 'G': '', 'H': 'H', 'I': 'I', 'J': 'L', 
        'K': '', 'L': 'J', 'M': 'M', 'N': '', 'O': 'O', 
        'P': '', 'Q': '', 'R': '', 'S': '2', 'T': 'T', 
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 
        'Z': '5', '1': '1', '2': 'S', '3': 'E', '4': '', 
        '5': 'Z', '6': '', '7': '', '8': '8', '9': '' 
    }

    try:
        while True:
            string = input()

            palindrome = True
            mirror = True
            strLen = len(string)

            if strLen == 0: return
            
            for i in range(strLen//2 + 1):
                if string[i] != string[strLen-i-1]:
                    palindrome = False
                    break

            for i in range(strLen//2 + 1):
                if reverses[string[i]] != string[strLen-i-1]:
                    mirror = False
                    break
            
            if palindrome:
                if mirror:
                    print(string.strip() + ' -- is a mirrored palindrome.')
                    print('')
                else:
                    print(string.strip() + ' -- is a regular palindrome.')
                    print('')
            else:
                if mirror:
                    print(string.strip() + ' -- is a mirrored string.')
                    print('')
                else:
                    print(string.strip() + ' -- is not a palindrome.')
                    print('')
    except EOFError:
        pass

if __name__ == '__main__':
    main()