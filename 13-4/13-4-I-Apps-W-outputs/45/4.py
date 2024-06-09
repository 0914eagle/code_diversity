
def get_max_sweets(n, s, x_y):
    # Sort the x_y list in descending order based on the first element of each tuple
    x_y.sort(key=lambda x: x[0], reverse=True)

    # Initialize the maximum number of sweets to 0
    max_sweets = 0

    # Iterate through the x_y list
    for i in range(n):
        # Unpack the current tuple
        x, y = x_y[i]

        # Check if the current type of sugar is within Caisa's budget
        if x <= s:
            # Calculate the number of sweets that Caisa can get as change
            sweets = s - x

            # Check if the number of sweets is greater than the current maximum
            if sweets > max_sweets:
                # Update the maximum number of sweets
                max_sweets = sweets

    # Return the maximum number of sweets
    return max_sweets

