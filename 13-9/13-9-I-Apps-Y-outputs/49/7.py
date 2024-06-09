
def polycarp(s):
    # Initialize a variable to store the maximum number of divisible numbers
    max_divisible = 0
    # Loop through each possible position for a cut
    for i in range(len(s)):
        # Check if the number at the current position is divisible by 3
        if int(s[i]) % 3 == 0:
            # If it is, add 1 to the maximum number of divisible numbers
            max_divisible += 1
        # Check if the current position is not the last position in the string
        if i != len(s) - 1:
            # If it is not, check if the number at the next position is divisible by 3
            if int(s[i + 1]) % 3 == 0:
                # If it is, add 1 to the maximum number of divisible numbers
                max_divisible += 1
    # Return the maximum number of divisible numbers
    return max_divisible

