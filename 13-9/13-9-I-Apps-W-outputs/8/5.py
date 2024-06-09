
def get_max_messiness(n, k):
    # Initialize a list to store the cows and their labels
    cows = list(range(1, n+1))
    # Initialize a variable to store the maximum messiness
    max_messiness = 0
    # Loop through each minute
    for i in range(k):
        # Swap the cows in the first and last stalls
        cows[0], cows[-1] = cows[-1], cows[0]
        # Calculate the messiness for this minute
        messiness = get_messiness(cows)
        # Update the maximum messiness if necessary
        max_messiness = max(max_messiness, messiness)
    # Return the maximum messiness
    return max_messiness

def get_messiness(cows):
    # Initialize a variable to store the messiness
    messiness = 0
    # Loop through each cow
    for i in range(len(cows)):
        # Loop through each cow after the current cow
        for j in range(i+1, len(cows)):
            # If the current cow is larger than the next cow, increment the messiness
            if cows[i] > cows[j]:
                messiness += 1
    # Return the messiness
    return messiness

