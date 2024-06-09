
import itertools

def solve(n, p, coders):
    # Initialize a set to store the possible suspects
    suspects = set()

    # Iterate over the coders' opinions
    for coder in coders:
        # Add the names of the coders to the set of suspects
        suspects.update(coder)

    # Use itertools.combinations to generate all possible pairs of suspects
    pairs = itertools.combinations(suspects, 2)

    # Initialize a counter to store the number of possible two-suspect sets
    count = 0

    # Iterate over the pairs of suspects
    for pair in pairs:
        # Initialize a set to store the coders who agree with the current pair
        agree = set()

        # Iterate over the coders' opinions
        for coder in coders:
            # If the current coder agrees with the current pair, add them to the set
            if pair[0] in coder or pair[1] in coder:
                agree.add(coder)

        # If the number of coders who agree with the current pair is at least p, increment the counter
        if len(agree) >= p:
            count += 1

    return count

n, p = map(int, input().split())
coders = [set(map(int, input().split())) for _ in range(n)]
print(solve(n, p, coders))

