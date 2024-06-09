
def solve(k):
    # Initialize variables
    name = ""
    min_length = 1000000

    # Iterate through all lowercase letters
    for c in range(97, 123):
        # Calculate the value of the current letter
        value = abs(c - 97)

        # Calculate the difference between the current letter and the previous letter
        if len(name) > 0:
            diff = abs(ord(name[-1]) - c)
            value += diff

        # If the current value is equal to the target value, add the current letter to the name
        if value == k:
            name += chr(c)
            break

        # If the current value is less than the target value, add the current letter to the name and continue
        elif value < k:
            name += chr(c)

    # If the name is empty, return "impossible"
    if not name:
        return "impossible"

    # Return the shortest string that encodes to the target value
    return name

