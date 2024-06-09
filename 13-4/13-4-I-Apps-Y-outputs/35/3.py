
def solve(n, k):
    # Initialize an empty string
    s = ""
    # Iterate from 1 to k
    for i in range(1, k+1):
        # Append the i-th letter of the alphabet to the string
        s += chr(i + 96)
    # Return the string
    return s

