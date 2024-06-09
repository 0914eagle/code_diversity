
def get_max_messiness(n, k):
    # Initialize the messiness array with 0s
    messiness = [0] * (n + 1)

    # Loop through each minute
    for minute in range(1, k + 1):
        # Get the current stall numbers
        stalls = list(range(1, n + 1))

        # Swap the first and last stalls
        stalls[0], stalls[n] = stalls[n], stalls[0]

        # Update the messiness array
        for i in range(n):
            messiness[stalls[i]] += n - i

    # Return the maximum messiness
    return max(messiness)

