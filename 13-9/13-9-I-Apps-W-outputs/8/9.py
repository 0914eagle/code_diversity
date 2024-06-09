
def get_max_messiness(n, k):
    # Initialize the messiness array with 0s
    messiness = [0] * (n + 1)

    # Loop through each minute
    for minute in range(1, k + 1):
        # Get the current stall numbers
        stalls = list(range(1, n + 1))

        # Swap the stalls
        stalls[minute % n] , stalls[(minute + 1) % n] = stalls[(minute + 1) % n] , stalls[minute % n]

        # Update the messiness array
        for i in range(1, n + 1):
            messiness[i] += 1 if stalls[i] > stalls[i - 1] else 0

    # Return the maximum messiness
    return max(messiness)

