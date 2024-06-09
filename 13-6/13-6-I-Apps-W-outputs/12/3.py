
def solve(a, b):
    # Initialize variables
    subsequence = ""
    i, j = 0, 0

    # Loop through both strings
    while i < len(a) and j < len(b):
        # If the current character in a is the same as the current character in b, add it to the subsequence
        if a[i] == b[j]:
            subsequence += a[i]
            i += 1
            j += 1
        # If the current character in a is not the same as the current character in b, skip the character in a
        else:
            i += 1

    # If the subsequence is empty, return a minus sign
    if not subsequence:
        return "-"

    return subsequence

