
def get_shuffles_required(n, cards):
    # Initialize a list to store the shuffles required
    shuffles_required = []
    
    # Loop through each card in the deck
    for i in range(n):
        # Get the current card and its position in the deck
        card = cards[i]
        position = i + 1
        
        # If the card is not in its correct position, add a shuffle to the list
        if card != position:
            shuffles_required.append(card)
    
    # Return the minimum number of shuffles required to put the deck in the given order
    return len(shuffles_required)

def main():
    # Read the number of cards and the deck order from stdin
    n = int(input())
    cards = list(map(int, input().split()))
    
    # Call the get_shuffles_required function and print the result
    print(get_shuffles_required(n, cards))

if __name__ == '__main__':
    main()

