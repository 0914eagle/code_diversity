
def solve(N, molecule):
    # Initialize variables
    count = 0
    other_char = 'B' if molecule[0] == 'A' else 'A'

    # Iterate through the molecule and count the number of mutations needed
    for i in range(N):
        if molecule[i] != other_char:
            count += 1
        other_char = 'B' if other_char == 'A' else 'A'

    return count

