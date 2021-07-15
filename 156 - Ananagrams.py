from collections import Counter 

def main():
    wordCount = Counter()
    words = []

    while True:
        string = input()
        string.strip()

        if string == '#':
            break

        for word in string.split():
            sortedWord = ''.join(sorted(word.lower()))

            if len(word) >= 1:
                wordCount[sortedWord] += 1

            words.append((word, sortedWord))

    ananagrams = []

    for word, sortedWord in words:
        if not sortedWord in wordCount or wordCount[sortedWord] < 2:
            ananagrams.append(word)

    print('\n'.join(sorted(ananagrams)))

if __name__ == '__main__':
    main()