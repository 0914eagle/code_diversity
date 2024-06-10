
def get_cards(oranges, apples):
    if oranges == 0 and apples == 0:
        return "Impossible"
    
    cards = []
    while oranges > 0 or apples > 0:
        if oranges > 0:
            cards.append("A")
            oranges -= 1
        if apples > 0:
            cards.append("B")
            apples -= 1
    
    return "".join(cards)

def get_compressed_cards(oranges, apples):
    cards = get_cards(oranges, apples)
    if cards == "Impossible":
        return cards
    
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count))
            compressed_cards.append(cards[i])
            count = 1
    
    compressed_cards.append(str(count))
    compressed_cards.append(cards[-1])
    
    return "".join(compressed_cards)

def main():
    oranges, apples = map(int, input().split())
    print(get_compressed_cards(oranges, apples))

if __name__ == '__main__':
    main()

