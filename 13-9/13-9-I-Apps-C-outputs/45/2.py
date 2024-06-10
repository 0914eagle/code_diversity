
def get_suspects(n, p, coders):
    # Initialize a set to store the suspects
    suspects = set()

    # Iterate over the coders
    for coder in coders:
        # If the coder agrees with the head's choice, add their choice to the suspects set
        if coder[0] in suspects or coder[1] in suspects:
            suspects.add(coder[0])
            suspects.add(coder[1])

    # Return the number of possible two-suspect sets
    return len(suspects)

def get_possible_two_suspect_sets(n, p, coders):
    # Initialize a set to store the possible two-suspect sets
    possible_two_suspect_sets = set()

    # Iterate over the coders
    for coder in coders:
        # If the coder agrees with the head's choice, add their choice to the possible two-suspect sets set
        if coder[0] in suspects or coder[1] in suspects:
            possible_two_suspect_sets.add((coder[0], coder[1]))

    # Return the number of possible two-suspect sets
    return len(possible_two_suspect_sets)

if __name__ == '__main__':
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coders.append(tuple(map(int, input().split())))
    print(get_possible_two_suspect_sets(n, p, coders))

