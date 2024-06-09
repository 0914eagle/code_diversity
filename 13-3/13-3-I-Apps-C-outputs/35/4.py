
def f1(y, l):
    # Initialize the largest base b
    b = 1
    # Loop through all possible bases
    for b in range(2, 11):
        # Convert y to base b
        y_b = int(y, b)
        # Check if y_b contains only decimal digits
        if all(0 <= i <= 9 for i in str(y_b)):
            # Check if y_b is at least l
            if y_b >= l:
                # If both conditions are met, return b
                return b
    # If no base meets the conditions, return -1
    return -1

