
def solve(n, memory):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a1, a2) in enumerate(memory, 1):
        remembered[i].add(a1)
        remembered[i].add(a2)

    # Initialize a set to store the kids that have been placed in the circle
    placed = set()

    # Initialize the permutation of kids
    permutation = [0] * (n + 1)

    # Start placing kids in the circle
    current_kid = 1
    while len(placed) < n:
        # Get the remembered kids for the current kid
        remembered_kids = remembered[current_kid]

        # Find the first remembered kid that has not been placed yet
        for kid in remembered_kids:
            if kid not in placed:
                break
        else:
            # If all remembered kids have been placed, start over from the beginning
            current_kid = 1
            continue

        # Place the current kid next to the remembered kid
        permutation[current_kid] = kid
        placed.add(current_kid)
        placed.add(kid)

        # Move on to the next kid
        current_kid = kid

    return permutation

