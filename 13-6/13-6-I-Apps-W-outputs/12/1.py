
def solve(a, b):
    # Initialize variables
    subsequence = ""
    i, j = 0, 0

    # Loop through both strings
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            # If characters match, add them to the subsequence
            subsequence += a[i]
            i += 1
            j += 1
        else:
            # If characters don't match, move on to the next character in string a
            i += 1

    # If we reach the end of string a and string b, return the subsequence
    if i == len(a) and j == len(b):
        return subsequence

    # If we reach the end of string a but not string b, return -
    if i == len(a) and j < len(b):
        return "-"

    # If we reach the end of string b but not string a, return the subsequence
    if j == len(b) and i < len(a):
        return subsequence

    # If we reach neither the end of string a nor string b, return -
    return "-"

