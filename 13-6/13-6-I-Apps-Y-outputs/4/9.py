
def solve(s, k):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    j = 0

    # Loop through the string
    while i < n and j < k:
        # If the current character is not 'R', 'G', or 'B', increase the count
        if s[i] != "R" and s[i] != "G" and s[i] != "B":
            count += 1
        # If the current character is 'R', 'G', or 'B', and the substring is not a substring of "RGB", increase the count
        elif s[i] == "R" and s[i + 1] != "G" or s[i] == "G" and s[i + 1] != "B" or s[i] == "B" and s[i + 1] != "R":
            count += 1
        # If the current character is 'R', 'G', or 'B', and the substring is a substring of "RGB", increase the count
        elif s[i] == "R" and s[i + 1] == "G" and s[i + 2] == "B" or s[i] == "G" and s[i + 1] == "B" and s[i + 2] == "R" or s[i] == "B" and s[i + 1] == "R" and s[i + 2] == "G":
            count += 2
        # Increase the indices
        i += 1
        j += 1

    # Return the count
    return count

