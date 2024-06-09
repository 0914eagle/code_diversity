
def solve(s):
    # Initialize variables
    k = 0
    n = len(s)
    result = s

    # Loop until the string is a palindrome or the maximum number of operations is reached
    while k < 30 and result != result[::-1]:
        # Check if the first operation can be applied
        if n - 1 > 1:
            # Append the substring reversed to the front of the string
            result = result[1:] + result[:1]
            k += 1
            # Print the operation
            print("L", 1)
        # Check if the second operation can be applied
        if n - 1 > 1:
            # Append the substring reversed to the end of the string
            result = result + result[-1:]
            k += 1
            # Print the operation
            print("R", n)

    # Return the number of operations performed
    return k

