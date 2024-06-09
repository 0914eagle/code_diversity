
def plush_toys(x, y):
    # Initialize variables
    original_toys = 1
    copied_toys = 0

    # Loop until the desired configuration is reached
    while original_toys + copied_toys < x + y:
        # If the number of original toys is odd, apply the machine to an original toy
        if original_toys % 2 == 1:
            original_toys += 1
            copied_toys += 2
        # If the number of original toys is even, apply the machine to a copy
        else:
            copied_toys += 1
            original_toys += 2

    # Return "Yes" if the desired configuration is possible, and "No" otherwise
    if original_toys == x and copied_toys == y:
        return "Yes"
    else:
        return "No"

