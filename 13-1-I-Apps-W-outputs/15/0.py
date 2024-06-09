
def solve(s):
    # Initialize variables
    k = 0
    n = len(s)
    result = s

    # Loop until the string is a palindrome or the maximum number of operations is reached
    while k < 30 and result != result[::-1]:
        # Check if the first operation can be applied
        if n > 2 and s[:n//2] == s[:n//2][::-1]:
            # Apply the first operation
            result = s[:n//2] + s[n//2:]
            k += 1
            print("L", n//2)
        # Check if the second operation can be applied
        elif n > 2 and s[n//2+1:] == s[n//2+1:][::-1]:
            # Apply the second operation
            result = s[:n//2+1] + s[n//2+1:][::-1]
            k += 1
            print("R", n//2+1)
        # If neither operation can be applied, break the loop
        else:
            break

    # Return the number of operations performed
    return k

