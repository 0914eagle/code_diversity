
def solve(s, t):
    # Initialize variables
    n = len(s)
    count = 0
    # Loop through each character of s and t
    for i in range(n):
        # If the characters are not equal, increment the count
        if s[i] != t[i]:
            count += 1
    # Return the count
    return count

