
def solve(n, memory):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a1, a2) in enumerate(memory, 1):
        remembered[i].add(a1)
        remembered[i].add(a2)

    # Initialize a set to store the kids that have been placed in the circle
    placed = set()

    # Start placing kids in the circle, starting with the kid that remembered the least number of kids
    current = min(remembered, key=lambda i: len(remembered[i]))
    placed.add(current)
    circle = [current]

    # While there are still kids to place in the circle
    while len(placed) < n:
        # Get the next kid to place in the circle
        next_kid = remembered[current].difference(placed).pop()
        placed.add(next_kid)
        circle.append(next_kid)

        # Update the remembered kids for the current kid
        remembered[current].remove(next_kid)
        if not remembered[current]:
            del remembered[current]

        # Set the current kid to the next kid
        current = next_kid

    return circle

