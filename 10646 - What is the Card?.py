def value(card):
	if card[0] in ['A','K','Q','J','T']:
		return 10

	return int(card[0])

def main():
    outputs = []

    cases = int(input())
    
    for c in range(cases):
        cards = input().strip().split()
        
        cardsHand = cards[27:52]
        pile = cards[0:27]

        y = 0

        for _ in range(1,4):
            pileSize = len(pile)
            x = value(pile[pileSize - 1])

            dropedCards = (10 - x) + 1
            pile = pile[0:pileSize - dropedCards]

            y += x

        cards = pile + cardsHand
        
        outputs.append("Case %s: %s"%(c + 1, cards[y - 1]))

    for item in outputs:
        print(item)

if __name__ == '__main__':
    main()