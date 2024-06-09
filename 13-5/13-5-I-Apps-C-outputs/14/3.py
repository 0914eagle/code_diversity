
def solve(n, debts):
    # Initialize a dictionary to store the debts
    debt_dict = {}
    for i in range(n):
        debt_dict[i+1] = 0
    
    # Iterate through the debts and update the dictionary
    for debt in debts:
        debt_dict[debt[0]] += debt[1]
        debt_dict[debt[1]] -= debt[1]
    
    # Initialize a set to store the visited nodes
    visited = set()
    
    # Initialize a queue to store the nodes to visit
    queue = []
    
    # Add the first node to the queue
    queue.append(1)
    
    # Loop until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the node has not been visited before, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            for neighbor in range(1, n+1):
                if neighbor not in visited and debt_dict[neighbor] > 0:
                    queue.append(neighbor)
    
    # Return the sum of the debts of the visited nodes
    return sum([debt_dict[node] for node in visited])

