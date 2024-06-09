
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the number of integers that can be written on the card
    num_integers = 0

    # Check if the cards can form an arithmetic progression
    if n == 1:
        return [-1]
    elif n == 2:
        if cards[1] - cards[0] == 1:
            return [-1]
        else:
            return [cards[1] - cards[0] - 1]
    else:
        # Calculate the difference between the first two cards
        diff = cards[1] - cards[0]

        # Check if the difference is equal to the difference between the second and third cards
        if diff == cards[2] - cards[1]:
            # Initialize the number that can be written on the card
            num = cards[0] + diff

            # Check if the number is a valid integer
            if num % 1 == 0:
                num_integers += 1
                integers = [num]

            # Check if the number is a valid integer and if it is not already in the list of integers
            while num_integers < n - 1 and num not in integers:
                num_integers += 1
                integers.append(num)
                num += diff

                # Check if the number is a valid integer
                if num % 1 == 0:
                    integers.append(num)

            # Return the list of integers
            return integers
        else:
            return [-1]

