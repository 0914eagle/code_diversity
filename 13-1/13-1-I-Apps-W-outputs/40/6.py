
def solve(N, A):
    # Sort the array in descending order
    A.sort(reverse=True)
    # Initialize the maximum number of remaining cards
    max_cards = 0
    # Loop through the array and find the maximum number of remaining cards
    for i in range(N-1):
        # If the current card is different from the previous card, increment the maximum number of remaining cards
        if A[i] != A[i+1]:
            max_cards += 1
    # Return the maximum number of remaining cards
    return max_cards

