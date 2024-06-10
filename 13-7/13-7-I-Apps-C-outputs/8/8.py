
def get_winner(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop through each card
    for i in range(n):
        # Check if the card is facing up
        if cards[i] == "1":
            # If the card is facing up, check if the next k-1 cards are all facing up
            for j in range(i+1, min(n, i+k)):
                if cards[j] == "0":
                    break
            else:
                # If all the next k-1 cards are facing up, return "tokitsukaze"
                return "tokitsukaze"
        # Check if the card is facing down
        if cards[i] == "0":
            # If the card is facing down, check if the previous k-1 cards are all facing down
            for j in range(max(0, i-k+1), i):
                if cards[j] == "1":
                    break
            else:
                # If all the previous k-1 cards are facing down, return "quailty"
                return "quailty"
    
    # If the game has not ended after all the cards have been checked, return "once again"
    return "once again"

def main():
    n, k = map(int, input().split())
    cards = input()
    print(get_winner(n, k, cards))

if __name__ == '__main__':
    main()

