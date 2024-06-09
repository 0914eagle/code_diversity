
def get_min_mutations(n, molecule):
    # Initialize variables
    count = 0
    other_character = 'B' if molecule[0] == 'A' else 'A'

    # Iterate through the molecule and count the number of mutations needed
    for i in range(n):
        if molecule[i] != other_character:
            count += 1

    return count

