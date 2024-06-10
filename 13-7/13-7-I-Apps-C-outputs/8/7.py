
def get_winner(n, k, cards):
    # Initialize the winner and the number of moves
    winner = "draw"
    moves = 0

    # Loop through each card and check if it can be flipped
    for i in range(n):
        # Check if the card is already face up or down
        if cards[i] == "0" or cards[i] == "1":
            continue

        # Check if the card can be flipped
        if i + k - 1 < n and cards[i + k - 1] == "0" or cards[i + k - 1] == "1":
            continue

        # Flip the card and update the winner
        cards[i] = "1" if cards[i] == "0" else "0"
        winner = "tokitsukaze" if cards.count("1") > cards.count("0") else "quailty"
        moves += 1

        # Check if the game is over
        if moves > 1000000000:
            winner = "draw"
            break

    return winner

def main():
    # Read the input
    n, k = map(int, input().split())
    cards = list(input())

    # Get the winner
    winner = get_winner(n, k, cards)

    # Print the result
    print(winner)

if __name__ == '__main__':
    main()

