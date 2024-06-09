
def solve(N):
    # Initialize the minimum number of banknotes to be used
    min_banknotes = 1000001
    # Loop through all possible values of banknotes
    for i in range(1, 1000001):
        # Calculate the number of banknotes needed by the clerk
        clerk_banknotes = N // (10 ** i)
        # Calculate the number of banknotes needed by you
        your_banknotes = N - (clerk_banknotes * (10 ** i))
        # Calculate the total number of banknotes used
        total_banknotes = clerk_banknotes + your_banknotes
        # Update the minimum number of banknotes if necessary
        if total_banknotes < min_banknotes:
            min_banknotes = total_banknotes
    # Return the minimum number of banknotes used
    return min_banknotes

