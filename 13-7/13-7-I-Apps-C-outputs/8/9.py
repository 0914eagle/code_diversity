
def check_game(n, k, cards):
    # Initialize the number of moves
    moves = 0
    
    # Initialize the number of cards with color sides facing up
    num_up = cards.count("1")
    
    # Loop through each card
    for i in range(n):
        # Check if the current card has the same color side as the previous card
        if i > 0 and cards[i] == cards[i-1]:
            # If so, increase the number of moves
            moves += 1
        # Check if the current card has the same color side as the next card
        if i < n-1 and cards[i] == cards[i+1]:
            # If so, increase the number of moves
            moves += 1
    
    # Check if the number of moves is less than or equal to the number of cards
    if moves <= n:
        # If so, return "once again"
        return "once again"
    
    # Check if the number of cards with color sides facing up is even
    if num_up % 2 == 0:
        # If so, return "quailty"
        return "quailty"
    # Otherwise, return "tokitsukaze"
    return "tokitsukaze"

def main():
    # Read the input
    n, k = map(int, input().split())
    cards = input()
    
    # Check the game
    result = check_game(n, k, cards)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

