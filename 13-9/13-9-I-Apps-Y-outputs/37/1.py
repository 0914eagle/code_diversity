
def solve(a, k):
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the current value of x to 0
    x = 0
    # Loop through each element of the array
    for i in range(len(a)):
        # If the current element is not divisible by k, we need to make moves
        if a[i] % k != 0:
            # Calculate the number of moves needed to make the current element divisible by k
            moves += k - a[i] % k
            # Increase the current value of x by 1
            x += 1
            # Add x to the current element
            a[i] += x
    # Return the total number of moves
    return moves

