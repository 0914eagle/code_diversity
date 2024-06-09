
def f1(y, l):
    # Initialize the largest base b
    b = 1
    # Loop through all possible bases
    for i in range(2, 10):
        # Convert y to base i
        y_i = int(y, i)
        # Check if y_i contains only decimal digits
        if all(0 <= digit <= 9 for digit in str(y_i)):
            # Check if y_i is at least l
            if y_i >= l:
                # Update the largest base b
                b = i
                break
    return b

