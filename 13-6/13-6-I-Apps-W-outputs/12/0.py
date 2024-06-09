
def solve(a, b):
    # Initialize variables
    subsequence = ""
    i, j = 0, 0

    # Loop through both strings
    while i < len(a) and j < len(b):
        # If the current character in a is equal to the current character in b, add it to the subsequence
        if a[i] == b[j]:
            subsequence += a[i]
            i += 1
            j += 1
        # If the current character in a is not equal to the current character in b, move on to the next character in a
        else:
            i += 1

    # If the subsequence is empty, return a minus sign
    if not subsequence:
        return "-"

    return subsequence

