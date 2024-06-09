
def solve(A, B, C, K):
    # Initialize a list to store the values of the cards
    cards = [1] * A + [0] * B + [-1] * C
    # Sort the list in descending order
    cards.sort(reverse=True)
    # Initialize a variable to store the sum
    sum = 0
    # Iterate through the first K elements of the list
    for i in range(K):
        # Add the current element to the sum
        sum += cards[i]
    # Return the sum
    return sum

