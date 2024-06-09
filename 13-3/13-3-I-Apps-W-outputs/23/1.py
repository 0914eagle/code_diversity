
def solve(N, molecule):
    # Initialize variables
    count = 0
    other_character = 'B' if molecule[0] == 'A' else 'A'

    # Iterate through the molecule and count the number of mutations needed
    for i in range(N):
        if molecule[i] != other_character:
            count += 1
        other_character = 'B' if other_character == 'A' else 'A'

    return count

