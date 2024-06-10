
def get_possible_suspects(n, p, coders):
    # Initialize a set to store the possible suspects
    possible_suspects = set()

    # Iterate over each coder
    for coder in coders:
        # If the coder agrees with the head's choice, add their names to the set of possible suspects
        if coder[0] in possible_suspects or coder[1] in possible_suspects:
            possible_suspects.add(coder[0])
            possible_suspects.add(coder[1])

    # Return the number of possible suspects
    return len(possible_suspects)

def get_number_of_two_suspect_sets(n, p, coders):
    # Get the possible suspects
    possible_suspects = get_possible_suspects(n, p, coders)

    # Initialize a set to store the two-suspect sets
    two_suspect_sets = set()

    # Iterate over each possible suspect
    for suspect in possible_suspects:
        # Add the suspect to the set of two-suspect sets
        two_suspect_sets.add((suspect, suspect))

        # Add the suspect to the set of two-suspect sets along with each of their neighbors
        for neighbor in possible_suspects - {suspect}:
            two_suspect_sets.add((suspect, neighbor))

    # Return the number of two-suspect sets
    return len(two_suspect_sets)

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        x, y = map(int, input().split())
        coders.append((x, y))
    print(get_number_of_two_suspect_sets(n, p, coders))

