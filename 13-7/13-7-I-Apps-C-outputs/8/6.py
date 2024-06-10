
def check_winner(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop through each card and check if it is facing up or down
    for i in range(n):
        # If the card is facing up, check if the next k-1 cards are also facing up
        if cards[i] == 1:
            # If all the next k-1 cards are facing up, increment the number of moves
            if all(cards[i+1:i+k]):
                moves += 1
        # If the card is facing down, check if the next k-1 cards are also facing down
        elif cards[i] == 0:
            # If all the next k-1 cards are facing down, increment the number of moves
            if all(cards[i+1:i+k] == 0):
                moves += 1
    
    # If the number of moves is even, return "tokitsukaze"
    if moves % 2 == 0:
        return "tokitsukaze"
    # If the number of moves is odd, return "quailty"
    else:
        return "quailty"

def main():
    # Read the input n and k
    n, k = map(int, input().split())
    # Read the input cards
    cards = list(map(int, input()))
    
    # Check if the total number of moves will exceed 10^9
    if n * k > 10**9:
        print("once again")
    # If not, check the winner and print the result
    else:
        print(check_winner(n, k, cards))

if __name__ == '__main__':
    main()

