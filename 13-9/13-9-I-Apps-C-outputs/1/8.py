
def get_min_waste(cards, envelopes):
    # Initialize the minimum waste to a large value
    min_waste = float('inf')
    
    # Iterate over all possible combinations of envelope sizes
    for envelope_size in combinations(cards, envelopes):
        # Calculate the total waste for this combination of envelopes
        total_waste = 0
        for card in cards:
            # Calculate the waste for this card
            waste = envelope_size - card
            total_waste += waste * waste
        
        # If the total waste is smaller than the current minimum, update the minimum waste
        if total_waste < min_waste:
            min_waste = total_waste
    
    # Return the minimum waste
    return min_waste

def main():
    # Read the number of cards and envelopes
    n, k = map(int, input().split())
    
    # Read the cards
    cards = []
    for _ in range(n):
        w, h, q = map(int, input().split())
        cards.append((w, h, q))
    
    # Call the get_min_waste function and print the result
    print(get_min_waste(cards, k))

if __name__ == '__main__':
    main()

