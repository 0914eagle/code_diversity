
def solve(n, k, card_state):
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of flips to 0
    flips = 0
    # Initialize the number of cards with color sides facing up to 0
    up = 0
    # Initialize the number of cards with color sides facing down to 0
    down = 0
    # Initialize the number of consecutive cards with the same color side facing up or down to 0
    consecutive = 0
    # Iterate through the cards
    for i in range(n):
        # Check if the current card has a color side facing up
        if card_state[i] == "1":
            # Increment the number of cards with color sides facing up
            up += 1
            # Check if the current card is the first card with a color side facing up
            if up == 1:
                # Increment the number of consecutive cards with the same color side facing up
                consecutive += 1
            # Check if the current card is the last card with a color side facing up
            elif up == k:
                # Increment the number of flips
                flips += 1
                # Reset the number of consecutive cards with the same color side facing up to 0
                consecutive = 0
            # Check if the current card is in the middle of a sequence of k consecutive cards with the same color side facing up
            elif consecutive == k - 1:
                # Increment the number of flips
                flips += 1
                # Reset the number of consecutive cards with the same color side facing up to 0
                consecutive = 0
        # Check if the current card has a color side facing down
        elif card_state[i] == "0":
            # Increment the number of cards with color sides facing down
            down += 1
            # Check if the current card is the first card with a color side facing down
            if down == 1:
                # Increment the number of consecutive cards with the same color side facing down
                consecutive -= 1
            # Check if the current card is the last card with a color side facing down
            elif down == k:
                # Increment the number of flips
                flips += 1
                # Reset the number of consecutive cards with the same color side facing down to 0
                consecutive = 0
            # Check if the current card is in the middle of a sequence of k consecutive cards with the same color side facing down
            elif consecutive == -k + 1:
                # Increment the number of flips
                flips += 1
                # Reset the number of consecutive cards with the same color side facing down to 0
                consecutive = 0
        # Increment the number of moves
        moves += 1
        # Check if the total number of moves exceeds 10^9
        if moves > 10**9:
            return "once again"
    # Check if Tokitsukaze can win
    if flips % 2 == 0:
        return "tokitsukaze"
    # Check if Quailty can win
    elif flips % 2 == 1:
        return "quailty"
    # Check if the game can end in a draw
    else:
        return "once again"

def main():
    n, k = map(int, input().split())
    card_state = input()
    print(solve(n, k, card_state))

if __name__ == '__main__':
    main()

