
def get_winner(n, k, cards):
    # Initialize the winner as None
    winner = None
    
    # Loop through each card and check if it is facing up or down
    for i in range(n):
        # If the card is facing up, check if it is the first card or the previous card is facing down
        if cards[i] == "1" and (i == 0 or cards[i-1] == "0"):
            # If it is the first card or the previous card is facing down, flip the next k-1 cards to the same side
            for j in range(i+1, i+k):
                if j < n:
                    cards[j] = "1" if cards[j] == "0" else "0"
    
    # Check if all the cards are facing the same direction
    if all(cards[i] == cards[0] for i in range(n)):
        # If they are, the winner is Tokitsukaze
        winner = "tokitsukaze"
    elif all(cards[i] != cards[0] for i in range(n)):
        # If they are not, the winner is Quailty
        winner = "quailty"
    
    return winner

def main():
    n, k = map(int, input().split())
    cards = list(input())
    winner = get_winner(n, k, cards)
    print(winner)

if __name__ == '__main__':
    main()

