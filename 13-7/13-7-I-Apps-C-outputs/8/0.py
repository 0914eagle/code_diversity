
def check_winner(n, k, cards):
    # Initialize variables
    num_moves = 0
    total_flips = 0
    flip_counts = [0] * n
    flip_sides = [0] * n
    flip_colors = [0] * n

    # Loop through each card
    for i in range(n):
        # Check if card is facing up
        if cards[i] == "1":
            # Increment total flips
            total_flips += 1

            # Check if card is part of a group of k consecutive cards
            if i - k + 1 >= 0 and cards[i - k + 1] == "1":
                # Increment flip count
                flip_counts[i] += 1

                # Check if flip count is equal to k
                if flip_counts[i] == k:
                    # Increment number of moves
                    num_moves += 1

                    # Check if number of moves is greater than 10^9
                    if num_moves > 10**9:
                        return "once again"

                    # Check if flip side is the same for all k cards
                    flip_side = cards[i]
                    for j in range(i - k + 1, i + 1):
                        if cards[j] != flip_side:
                            flip_side = -1
                            break

                    # Check if flip side is the same for all k cards
                    if flip_side == "1":
                        return "tokitsukaze"
                    elif flip_side == "0":
                        return "quailty"

    # Check if total number of flips is even
    if total_flips % 2 == 0:
        return "quailty"
    else:
        return "tokitsukaze"

def main():
    # Read input
    n, k = map(int, input().split())
    cards = input()

    # Check winner
    winner = check_winner(n, k, cards)

    # Print winner
    print(winner)

if __name__ == '__main__':
    main()

