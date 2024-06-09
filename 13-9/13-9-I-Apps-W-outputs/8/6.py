
def get_max_messiness(n, k):
    # Initialize a list to store the cows in their initial order
    cows = list(range(1, n + 1))
    # Initialize a variable to store the maximum messiness
    max_messiness = 0
    # Loop through each minute
    for i in range(k):
        # Swap the cows in the first and last stalls
        cows[0], cows[-1] = cows[-1], cows[0]
        # Calculate the current messiness
        messiness = 0
        for j in range(n - 1):
            if cows[j] > cows[j + 1]:
                messiness += 1
        # Update the maximum messiness if necessary
        max_messiness = max(max_messiness, messiness)
    # Return the maximum messiness
    return max_messiness

