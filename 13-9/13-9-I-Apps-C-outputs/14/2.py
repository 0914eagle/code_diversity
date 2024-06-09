
import itertools

def get_number_of_suspects(n, p, coders):
    # Initialize a set to store the suspects
    suspects = set()

    # Iterate over the coders' statements
    for coder in coders:
        # Add the two suspects named by the current coder to the set
        suspects.update(coder)

    # Get the power set of the suspects (i.e. all possible subsets)
    power_set = itertools.combinations(suspects, 2)

    # Initialize a counter for the number of valid suspect sets
    count = 0

    # Iterate over the power set
    for suspect_set in power_set:
        # Initialize a set to store the coders who agreed with the current suspect set
        agreed_coders = set()

        # Iterate over the coders' statements
        for coder in coders:
            # If the current suspect set contains at least one of the two suspects named by the current coder, add the coder to the agreed_coders set
            if suspect_set[0] in coder or suspect_set[1] in coder:
                agreed_coders.add(coder)

        # If the number of agreed coders is greater than or equal to p, increment the counter
        if len(agreed_coders) >= p:
            count += 1

    return count

n, p = map(int, input().split())
coders = [set(map(int, input().split())) for _ in range(n)]
print(get_number_of_suspects(n, p, coders))

