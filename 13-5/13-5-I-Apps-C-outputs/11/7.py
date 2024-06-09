
def solve(n, a, b):
    # Initialize a list to store the current position of the statues
    current_pos = [0] * n
    for i in range(n):
        # If the current island has a statue, add it to the list
        if a[i] != 0:
            current_pos[i] = a[i]
    
    # Initialize a list to store the desired position of the statues
    desired_pos = [0] * n
    for i in range(n):
        # If the current island has a statue, add it to the list
        if b[i] != 0:
            desired_pos[i] = b[i]
    
    # Check if the current position and desired position are the same
    if current_pos == desired_pos:
        return "YES"
    
    # Initialize a set to store the visited islands
    visited = set()
    # Initialize a queue to store the next islands to visit
    queue = [0]
    # Loop until the queue is empty
    while queue:
        # Get the current island from the queue
        current_island = queue.pop(0)
        # If the current island has a statue and it is not in the desired position, move it
        if current_pos[current_island] != 0 and current_pos[current_island] != desired_pos[current_island]:
            # Get the adjacent island with an empty pedestal
            adjacent_island = (current_island + 1) % n
            while current_pos[adjacent_island] != 0:
                adjacent_island = (adjacent_island + 1) % n
            # Move the statue from the current island to the adjacent island
            current_pos[current_island] = 0
            current_pos[adjacent_island] = current_pos[current_island]
            # Add the current island to the visited set
            visited.add(current_island)
            # Add the adjacent island to the queue
            queue.append(adjacent_island)
    
    # Check if all the statues are in the desired position
    if current_pos == desired_pos:
        return "YES"
    else:
        return "NO"

