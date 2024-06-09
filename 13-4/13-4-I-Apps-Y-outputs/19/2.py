
def solve(n, memory):
    # Initialize a dictionary to map each kid to their remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a1, a2) in enumerate(memory, 1):
        remembered[i].add(a1)
        remembered[i].add(a2)

    # Initialize a set to keep track of the kids that have been placed in the circle
    placed = set()

    # Start placing kids in the circle, starting with the kid that remembered the least number of other kids
    while len(placed) < n:
        # Find the kid that remembered the least number of other kids and has not been placed yet
        current_kid = min(remembered, key=lambda x: len(remembered[x]) - len(placed))
        while current_kid in placed:
            current_kid = min(remembered, key=lambda x: len(remembered[x]) - len(placed))

        # Place the current kid in the circle
        placed.add(current_kid)

        # Remove the current kid from the dictionary of remembered kids
        del remembered[current_kid]

        # Add the current kid to the set of placed kids
        placed.add(current_kid)

        # Update the dictionary of remembered kids by removing the current kid and adding their remembered kids
        for kid in remembered:
            if current_kid in remembered[kid]:
                remembered[kid].remove(current_kid)

    # Return the permutation of kids in the circle
    return list(placed)

