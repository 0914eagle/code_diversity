
def get_hand_strength(hand):
    # Initialize a dictionary to keep track of the rank frequencies
    rank_freq = {}
    for card in hand:
        rank = card[0]
        if rank in rank_freq:
            rank_freq[rank] += 1
        else:
            rank_freq[rank] = 1
    
    # Find the maximum frequency
    max_freq = max(rank_freq.values())
    
    # Return the maximum frequency
    return max_freq

def main():
    hand = input("Enter five cards: ").split()
    print(get_hand_strength(hand))

if __name__ == '__main__':
    main()

