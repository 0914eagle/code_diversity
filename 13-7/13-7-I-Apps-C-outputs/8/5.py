
def get_winner(n, k, cards):
    # Initialize the variables
    num_moves = 0
    num_flips = 0
    num_same_sides = 0
    same_sides = []
    winner = ""

    # Loop through each card
    for i in range(n):
        # Check if the card is facing up
        if cards[i] == "1":
            # If the card is facing up, check if it is the same as the previous card
            if i > 0 and cards[i - 1] == "1":
                # If the card is the same as the previous card, add it to the list of same-sided cards
                same_sides.append(i)
            # If the card is not the same as the previous card, check if it is the same as the next card
            elif i < n - 1 and cards[i + 1] == "1":
                # If the card is the same as the next card, add it to the list of same-sided cards
                same_sides.append(i)
        # If the card is facing down, check if it is the same as the previous card
        elif i > 0 and cards[i - 1] == "0":
            # If the card is the same as the previous card, add it to the list of same-sided cards
            same_sides.append(i)
        # If the card is not the same as the previous card, check if it is the same as the next card
        elif i < n - 1 and cards[i + 1] == "0":
            # If the card is the same as the next card, add it to the list of same-sided cards
            same_sides.append(i)

    # Loop through each same-sided card
    for i in same_sides:
        # Check if the card is facing up
        if cards[i] == "1":
            # If the card is facing up, add 1 to the number of flips
            num_flips += 1
        # If the card is facing down, add 1 to the number of flips
        else:
            num_flips += 1

    # Check if the number of flips is greater than the number of moves
    if num_flips > num_moves:
        # If the number of flips is greater than the number of moves, return "once again"
        return "once again"
    # If the number of flips is not greater than the number of moves, return the winner
    else:
        # If the number of flips is not greater than the number of moves, return the winner
        if num_flips % 2 == 0:
            return "tokitsukaze"
        else:
            return "quailty"

def main():
    # Read the input
    n, k = map(int, input().split())
    cards = input()

    # Call the get_winner function
    winner = get_winner(n, k, cards)

    # Print the winner
    print(winner)

if __name__ == '__main__':
    main()

