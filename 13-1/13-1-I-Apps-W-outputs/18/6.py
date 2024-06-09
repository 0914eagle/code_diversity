
def get_max_length(p):
    # Initialize the maximum length of the array
    max_length = 1
    # Loop through each digit in p
    for digit in str(p):
        # If the digit is not zero, add it to the maximum length
        if digit != "0":
            max_length += 1
    return max_length

