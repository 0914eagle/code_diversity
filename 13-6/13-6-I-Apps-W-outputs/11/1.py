
def solve(s):
    # Initialize variables
    k = 0
    n = len(s)
    result = s

    # Loop until the string is a palindrome or the maximum number of operations is reached
    while k < 30 and result != result[::-1]:
        # Check if the first operation can be applied
        if n > 2 and s[1] != s[-2]:
            # Apply the first operation
            result = s[1] + s[:-1] + s[1]
            k += 1
            print("L", 1)
        # Check if the second operation can be applied
        elif n > 2 and s[0] != s[-1]:
            # Apply the second operation
            result = s[:-1] + s[-1] + s[0]
            k += 1
            print("R", n-1)
        # If both operations are not possible, return the current string
        else:
            return result

    # Return the final string
    return result

