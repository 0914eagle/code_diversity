
def get_max_remaining_cards(deck):
    
    # Sort the deck in descending order
    deck.sort(reverse=True)
    # Eat the two cards with the largest values
    largest_card = deck.pop()
    second_largest_card = deck.pop()
    # Eat the card with the smallest value
    smallest_card = deck.pop(0)
    # Return the remaining card to the deck
    deck.append(largest_card)
    # Return the number of remaining cards
    return len(deck)

def main():
    # Read the input deck from stdin
    deck = list(map(int, input().split()))
    # Find the maximum number of remaining cards
    max_remaining_cards = get_max_remaining_cards(deck)
    # Print the result
    print(max_remaining_cards)

if __name__ == '__main__':
    main()

