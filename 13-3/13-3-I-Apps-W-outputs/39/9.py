
def solve(N):
    # Initialize the minimum number of banknotes to infinity
    min_banknotes = float('inf')
    # Loop through all possible values of banknotes
    for banknote in range(1, 10**100+1):
        # Calculate the number of banknotes needed
        num_banknotes = N // banknote
        # If the number of banknotes is less than the minimum, update the minimum
        if num_banknotes < min_banknotes:
            min_banknotes = num_banknotes
    # Return the minimum number of banknotes
    return min_banknotes

