
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
            if current != 1 and p[current] in received:
                # Set the current officer to their direct superior
                current = p[current]
            # If the current officer does not have direct subordinates or all their direct subordinates have received the command
            else:
                # Set the current officer to the next officer in the order
                current = order.pop(0)
        
        # Add the current officer to the order
        order.append(current)
    
    # Return the k-th element of the order or -1 if there are fewer than k elements
    return order[query[1] - 1] if query[1] <= len(order) else -1

