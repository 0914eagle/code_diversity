
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
    
    # Initialize a set to store the visited islands
    visited = set()
    
    # Initialize a variable to store the number of steps
    steps = 0
    
    # Loop until the statues are in the desired position
    while current_pos != desired_pos:
        # Find the first island with a statue that is not in the desired position
        for i in range(n):
            if current_pos[i] != 0 and current_pos[i] != desired_pos[i]:
                break
        
        # If no such island is found, return "NO"
        if i == n:
            return "NO"
        
        # Find the adjacent island with an empty pedestal
        for j in range(i+1, n):
            if current_pos[j] == 0:
                break
        
        # If no such island is found, return "NO"
        if j == n:
            return "NO"
        
        # Move the statue from the current island to the adjacent island
        current_pos[i] = 0
        current_pos[j] = current_pos[i]
        visited.add(i)
        visited.add(j)
        steps += 1
    
    # If all the statues are in the desired position, return "YES"
    if steps == n - 1:
        return "YES"
    
    # If not all the statues are in the desired position, return "NO"
    return "NO"

