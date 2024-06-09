
def solve(n, s):
    # Initialize variables
    count = 0
    other = 'B' if s[0] == 'A' else 'A'

    # Iterate through the string and count the number of mutations needed
    for i in range(n):
        if s[i] != other:
            count += 1
        other = 'B' if other == 'A' else 'A'

    return count

