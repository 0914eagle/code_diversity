
def get_fruits(x, y):
    # Initialize variables
    oranges = x
    apples = y
    cards = []

    # Play the game
    while oranges > 0 and apples > 0:
        # Remove a card from the deck
        card = input("Enter a card: ")
        cards.append(card)

        # If the card is 'A', give all oranges to Bob and take apples from the bag
        if card == 'A':
            oranges = 0
            apples -= oranges

        # If the card is 'B', give all apples to Alice and take oranges from the bag
        elif card == 'B':
            apples = 0
            oranges -= apples

    # Compress the sequence of cards
    compressed_cards = []
    current_card = cards[0]
    count = 1
    for i in range(1, len(cards)):
        if cards[i] == current_card:
            count += 1
        else:
            compressed_cards.append(str(count) + current_card)
            current_card = cards[i]
            count = 1
    compressed_cards.append(str(count) + current_card)

    return "".join(compressed_cards)

def main():
    x, y = map(int, input("Enter the number of oranges and apples: ").split())
    print(get_fruits(x, y))

if __name__ == '__main__':
    main()

