
def get_max_messiness(n, k):
    # Initialize an array to store the cows
    cows = [i for i in range(1, n + 1)]
    # Initialize a variable to store the maximum messiness
    max_messiness = 0
    # Loop through each minute
    for minute in range(k):
        # Swap the cows in the first and last stalls
        cows[0], cows[-1] = cows[-1], cows[0]
        # Calculate the messiness for this minute
        messiness = 0
        for i in range(n - 1):
            if cows[i] > cows[i + 1]:
                messiness += 1
        # Update the maximum messiness
        max_messiness = max(max_messiness, messiness)
    # Return the maximum messiness
    return max_messiness

