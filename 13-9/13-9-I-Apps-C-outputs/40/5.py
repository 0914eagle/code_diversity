
def get_max_earned_yen(a):
    # Initialize the maximum amount of money to be earned to 0
    max_earned = 0
    # Loop through each element in the list a
    for i in range(len(a)):
        # Check if the current element is positive
        if a[i] > 0:
            # Add the current element to the maximum amount of money to be earned
            max_earned += a[i]
        # Check if the current element is negative
        elif a[i] < 0:
            # Subtract the current element from the maximum amount of money to be earned
            max_earned += a[i]
    # Return the maximum amount of money to be earned
    return max_earned

