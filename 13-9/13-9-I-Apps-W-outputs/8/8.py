
def get_max_messiness(n, k):
    # Initialize an array to store the cows and their labels
    cows = [i for i in range(1, n + 1)]
    # Initialize a variable to store the maximum messiness
    max_messiness = 0
    # Loop through each minute
    for minute in range(k):
        # Swap the cows in the first and last stalls
        cows[0], cows[n - 1] = cows[n - 1], cows[0]
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
        # Find the label of the cow in the i-th stall
        label = cows[i]
        # Loop through the remaining cows
        for j in range(i + 1, len(cows)):
            # Find the label of the cow in the j-th stall
            other_label = cows[j]
            # If the label of the cow in the i-th stall is greater than the label of the cow in the j-th stall
            if label > other_label:
                # Increment the messiness
                messiness += 1
    # Return the messiness
    return messiness

