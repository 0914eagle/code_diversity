
def solve(N):
    # Initialize the minimum number of banknotes to be used
    min_banknotes = 0
    # Iterate through the possible values of banknotes
    for banknote in range(1, 10**100+1):
        # Calculate the number of banknotes needed to make the payment
        num_banknotes = N // banknote
        # If the number of banknotes needed is less than the current minimum, update the minimum
        if num_banknotes < min_banknotes or min_banknotes == 0:
            min_banknotes = num_banknotes
        # If the number of banknotes needed is equal to the current minimum, update the minimum
        if num_banknotes == min_banknotes:
            min_banknotes = num_banknotes
    # Return the minimum number of banknotes used
    return min_banknotes

