
def solve(N):
    # Initialize the minimum number of banknotes to be used
    min_banknotes = 1000001
    # Loop through all possible values of banknotes
    for i in range(1, 1000001):
        # Calculate the number of banknotes needed to make the payment
        num_banknotes = N // i + (N % i > 0)
        # Update the minimum number of banknotes if necessary
        if num_banknotes < min_banknotes:
            min_banknotes = num_banknotes
    # Return the minimum number of banknotes used
    return min_banknotes

