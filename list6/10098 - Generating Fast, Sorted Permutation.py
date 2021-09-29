# -*- coding: UTF-8 -*-  
def generatePermutation(letters, current):
    if (len(letters) == 0):
        yield current
    else:
        uniqueLetters = set()

        for i in range(len(letters)):
            if not letters[i] in uniqueLetters:
                uniqueLetters.add(letters[i])

                yield from generatePermutation(letters[:i] + letters[i + 1:], current + letters[i])

def main():
    cases = int(input())

    for _ in range(cases):
        word = input()
        word = sorted(word)

        for word in generatePermutation(word, ''):
            print(word)

        print()
        
if __name__=='__main__':
	main()
