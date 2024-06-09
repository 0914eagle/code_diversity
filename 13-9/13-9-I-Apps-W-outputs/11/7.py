
def solve(k):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the alphabet (lowercase letters)
    for letter in string.ascii_lowercase:
        # Calculate the difference between the current letter and the target number
        diff = abs(ord(letter) - k)

        # If the difference is 0, then we have found the letter that encodes to the target number
        if diff == 0:
            return letter

        # If the difference is less than the current minimum difference, then we have found a better letter
        if diff < min_diff:
            min_diff = diff
            result = letter

    # Return the best letter that we have found
    return result

