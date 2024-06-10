
def get_winner(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop until all cards are face up or down
    while True:
        # Check if all cards are face up or down
        if all(cards[i] == cards[0] for i in range(n)):
            # If all cards are face up, Tokitsukaze wins
            if cards[0] == 1:
                return "tokitsukaze"
            # If all cards are face down, Quailty wins
            else:
                return "quailty"
        
        # Increment the number of moves
        moves += 1
        
        # Check if the number of moves exceeds 10^9
        if moves > 10**9:
            return "once again"
        
        # Choose the first k cards
        chosen_cards = cards[:k]
        
        # Flip the chosen cards
        for i in range(k):
            cards[i] = 1 - cards[i]
        
        # Shift the cards to the right
        cards = cards[k:] + cards[:k]
    
def main():
    n, k = map(int, input().split())
    cards = list(map(int, input()))
    print(get_winner(n, k, cards))
    
if __name__ == '__main__':
    main()

