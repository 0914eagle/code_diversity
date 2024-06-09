
def solve(k):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the alphabet (lowercase letters)
    for letter in string.ascii_lowercase:
        # Calculate the absolute difference between the current letter and the target number
        diff = abs(ord(letter) - k)

        # If the difference is zero, we have found the letter that encodes to the target number
        if diff == 0:
            return letter

        # If the difference is less than the current minimum difference, we have found a new minimum
        if diff < min_diff:
            min_diff = diff
            result = letter

    # Return the result
    return result

