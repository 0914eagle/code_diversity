
def solve(s, t):
    # Initialize variables
    n = len(s)
    count = 0
    diff = 0

    # Loop through each character of both strings
    for i in range(n):
        # If characters are not equal, increment count and find difference
        if s[i] != t[i]:
            count += 1
            if diff == 0:
                diff = ord(t[i]) - ord(s[i])
            elif ord(t[i]) - ord(s[i]) != diff:
                return -1

    # Return count
    return count

