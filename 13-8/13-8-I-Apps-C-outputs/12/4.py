
def get_possible_suspect_sets(n, p, coders):
    # Initialize a set to store the possible suspect sets
    suspect_sets = set()

    # Iterate over each coder
    for coder in coders:
        # Get the names of the suspects mentioned by the coder
        x, y = coder

        # If the coder has agreed with the head's choice, add the suspect set to the set of possible suspect sets
        if x in suspect_sets or y in suspect_sets:
            suspect_sets.add((x, y))

    # Return the number of possible suspect sets
    return len(suspect_sets)

def main():
    # Read the input
    n, p = map(int, input().split())
    coders = [tuple(map(int, input().split())) for _ in range(n)]

    # Find the possible suspect sets
    possible_suspect_sets = get_possible_suspect_sets(n, p, coders)

    # Print the number of possible suspect sets
    print(possible_suspect_sets)

if __name__ == '__main__':
    main()

