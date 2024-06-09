
def solve(n, memory):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i, (a, b) in enumerate(memory, 1):
        remembered[i].add(a)
        remembered[i].add(b)
    
    # Initialize a set to store the kids that have been placed in the circle
    placed = set()
    
    # Initialize the permutation as an empty list
    permutation = []
    
    # Start placing kids in the circle
    while len(permutation) < n:
        # Find the next kid to place in the circle
        for i in range(1, n + 1):
            if i not in placed and len(remembered[i]) == 2:
                # Get the two kids that the current kid remembers
                a, b = remembered[i]
                
                # Check if both kids have been placed in the circle
                if a in placed and b in placed:
                    # Place the current kid after the kid it remembers
                    permutation.append(i)
                    placed.add(i)
                    break
    
    return permutation

