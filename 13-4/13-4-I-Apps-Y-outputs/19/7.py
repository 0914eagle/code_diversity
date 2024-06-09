
def solve(n, memory):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a, b) in enumerate(memory, 1):
        remembered[i].add(a)
        remembered[i].add(b)
    
    # Initialize a set to store the kids that have been placed in the circle
    placed = set()
    
    # Initialize the permutation of kids
    permutation = [0] * (n + 1)
    
    # Start placing kids in the circle
    current = 1
    while len(placed) < n:
        # If the current kid has not been placed yet, place it in the circle
        if current not in placed:
            # Add the current kid to the placed set
            placed.add(current)
            # Add the current kid to the permutation
            permutation[current] = current
            # Move on to the next kid
            current = remembered[current].difference(placed).pop()
        # If the current kid has already been placed, move on to the next kid
        else:
            current = remembered[current].difference(placed).pop()
    
    return permutation[1:]

