
import math

def get_largest_pile(n, a):
    # Initialize the pile with all the boxes
    pile = list(range(1, n + 1))
    largest_pile = []

    # Loop through each box and check if it can be added to the pile
    for i in range(n):
        # Check if the current box is divisible by any of the previous boxes in the pile
        for j in range(len(pile)):
            if a[i] % a[pile[j] - 1] == 0:
                # Add the current box to the pile and break
                pile.append(i + 1)
                break
        else:
            # If the current box is not divisible by any of the previous boxes in the pile,
            # it cannot be added to the pile, so continue to the next box
            continue

        # If the current box is added to the pile, check if the pile is larger than the largest pile found so far
        if len(pile) > len(largest_pile):
            largest_pile = pile

    # Return the largest pile
    return largest_pile

def solve(n, a):
    # Get the largest pile
    largest_pile = get_largest_pile(n, a)

    # Calculate the number of distinct piles
    num_distinct_piles = math.factorial(len(largest_pile))

    # Return the number of distinct piles modulo 10^9 + 7
    return num_distinct_piles % (10**9 + 7)

