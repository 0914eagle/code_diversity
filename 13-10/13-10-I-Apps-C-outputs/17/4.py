
def get_winner(n, k, cards):
    # Initialize variables
    num_moves = 0
    num_flips = 0
    flip_direction = None
    flip_start = None
    flip_end = None
    winning_player = None

    # Loop through each card
    for i in range(n):
        # If the card is facing up and the flip direction is not set, set the flip direction to up
        if cards[i] == "1" and flip_direction is None:
            flip_direction = "up"
            flip_start = i

        # If the card is facing down and the flip direction is not set, set the flip direction to down
        elif cards[i] == "0" and flip_direction is None:
            flip_direction = "down"
            flip_start = i

        # If the flip direction is set and the card is facing the opposite direction, set the flip end
        elif cards[i] == ("1" if flip_direction == "down" else "0") and flip_direction is not None:
            flip_end = i

        # If the flip end is set and the number of flips is less than k, increment the number of flips
        if flip_end is not None and num_flips < k:
            num_flips += 1

        # If the number of flips is equal to k, check if the player who made the move will win
        if num_flips == k:
            # If the player who made the move will win, set the winning player
            if flip_direction == "up" and flip_start == 0 and flip_end == n-1:
                winning_player = "tokitsukaze"
            elif flip_direction == "down" and flip_start == n-1 and flip_end == 0:
                winning_player = "quailty"

            # Reset the flip variables
            flip_direction = None
            flip_start = None
            flip_end = None
            num_flips = 0

    # If the number of moves exceeds 10^9, return "once again"
    if num_moves > 10**9:
        return "once again"

    # If the winning player is not set, return "once again"
    if winning_player is None:
        return "once again"

    # Return the winning player
    return winning_player

def main():
    n, k = map(int, input().split())
    cards = input()
    print(get_winner(n, k, cards))

if __name__ == '__main__':
    main()

