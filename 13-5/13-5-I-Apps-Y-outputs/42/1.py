
def solve(n, q, p, queries):
    # Initialize a list to store the order of officers receiving the command
    order = []
    
    # Iterate over each query
    for query in queries:
        # Initialize a set to store the officers who have received the command
        received = set()
        
        # Initialize the current officer as the query officer
        current = query[0]
        
        # While the current officer has not received the command
        while current not in received:
            # Add the current officer to the set of received officers
            received.add(current)
            
            # If the current officer has direct subordinates
            if current != 1 and current in p:
                # Choose the direct subordinate with the minimum index
                current = min(p[current], key=lambda x: x[1])
            # Otherwise, the current officer has no direct subordinates
            else:
                # Set the current officer to -1
                current = -1
        
        # Add the current officer to the order list
        order.append(current)
    
    # Return the k-th element of the order list for each query
    return [order[query[1] - 1] if query[1] <= len(order) else -1 for query in queries]

