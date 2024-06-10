
def get_cards_sequence(oranges, apples):
    # Initialize variables
    cards = []
    cards_count = 0
    oranges_alice, apples_alice = oranges, apples
    oranges_bob, apples_bob = 0, 0

    # Loop until all fruit is gone
    while oranges_alice > 0 or apples_alice > 0:
        # Add card to sequence
        cards.append('A' if oranges_alice > apples_alice else 'B')
        cards_count += 1

        # Update fruit count
        if cards[-1] == 'A':
            oranges_bob += oranges_alice
            apples_bob += apples_alice
            oranges_alice, apples_alice = 0, 0
        else:
            oranges_alice += oranges_bob
            apples_alice += apples_bob
            oranges_bob, apples_bob = 0, 0

    # Compress sequence
    compressed_cards = ''
    current_card = cards[0]
    current_count = 1
    for i in range(1, cards_count):
        if cards[i] == current_card:
            current_count += 1
        else:
            compressed_cards += str(current_count) + current_card
            current_card = cards[i]
            current_count = 1
    compressed_cards += str(current_count) + current_card

    return compressed_cards

def main():
    oranges, apples = map(int, input().split())
    print(get_cards_sequence(oranges, apples))

if __name__ == '__main__':
    main()

