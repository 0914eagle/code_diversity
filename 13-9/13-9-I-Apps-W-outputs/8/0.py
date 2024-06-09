
def get_max_messiness(n, k):
    # Initialize a list to store the cows and their labels
    cows = list(range(1, n + 1))
    # Initialize a variable to store the maximum messiness
    max_messiness = 0
    # Loop through each minute
    for i in range(k):
        # Swap the cows in the first and last stalls
        cows[0], cows[-1] = cows[-1], cows[0]
        # Update the maximum messiness
        max_messiness = max(max_messiness, get_messiness(cows))
    # Return the maximum messiness
    return max_messiness

def get_messiness(cows):
    # Initialize a variable to store the messiness
    messiness = 0
    # Loop through each cow
    for i in range(len(cows)):
        # Find the index of the cow in the list
        index = cows.index(i + 1)
        # If the cow is not in the last position
        if index != len(cows) - 1:
            # Update the messiness
            messiness += len(cows) - index - 1
    # Return the messiness
    return messiness

