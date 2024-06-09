
def solve(n, memory):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a1, a2) in enumerate(memory, 1):
        remembered[i].add(a1)
        remembered[i].add(a2)

    # Initialize a set to keep track of the kids that have been placed in the circle
    placed = set()

    # Start with the first kid and place it in the circle
    current = 1
    circle = [current]
    placed.add(current)

    # While there are still kids to place in the circle
    while len(placed) < n:
        # Get the remembered kids for the current kid
        remembered_kids = remembered[current] - placed

        # If the current kid has no remembered kids, it means it is the last kid in the circle
        if not remembered_kids:
            break

        # Get the next kid to place in the circle, which is the first remembered kid that has not been placed yet
        next_kid = min(remembered_kids - placed)
        circle.append(next_kid)
        placed.add(next_kid)

        # Set the current kid to the next kid
        current = next_kid

    return circle

