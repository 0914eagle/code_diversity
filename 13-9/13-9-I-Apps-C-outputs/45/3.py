
def get_suspects(n, p, coders):
    # Initialize a set to store the suspects
    suspects = set()

    # Iterate over the coders and their named suspects
    for coder, x, y in coders:
        # If the coder named both suspects, add them to the set
        if x in (x, y) and y in (x, y):
            suspects.add(x)
            suspects.add(y)

    # Return the number of suspects that are agreed upon by at least p coders
    return len([suspect for suspect in suspects if suspect in coders.keys()]) >= p

def count_two_suspect_sets(n, p, coders):
    # Initialize a set to store the two-suspect sets
    two_suspect_sets = set()

    # Iterate over the coders and their named suspects
    for coder, x, y in coders:
        # If the coder named both suspects, add them to the set
        if x in (x, y) and y in (x, y):
            two_suspect_sets.add((x, y))

    # Return the number of two-suspect sets that have at least p coders agreeing on them
    return len([two_suspect_set for two_suspect_set in two_suspect_sets if get_suspects(n, p, {coder: two_suspect_set for coder in coders})])

def main():
    n, p = map(int, input().split())
    coders = [tuple(map(int, input().split())) for _ in range(n)]
    print(count_two_suspect_sets(n, p, coders))

if __name__ == '__main__':
    main()

