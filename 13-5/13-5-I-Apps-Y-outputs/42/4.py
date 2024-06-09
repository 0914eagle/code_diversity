
def solve(n, q, p, queries):
    # Initialize a list to store the order in which officers receive the command
    order = []
    
    # Iterate over each query
    for query in queries:
        # Initialize a set to store the indices of the officers who have received the command
        received = set()
        
        # Initialize the current officer as the query officer
        current = query[0]
        
        # Iterate until the command is spread to all officers
        while len(received) < n:
            # Add the current officer to the set of received officers
            received.add(current)
            
            # If the current officer has direct subordinates, choose the subordinate with the minimum index
            if current in p:
                current = min(p[current], key=lambda x: x not in received)
            # Otherwise, the command has been spread to all officers
            else:
                break
            
            # Add the current officer to the order list
            order.append(current)
        
        # Print the required officer in the order list or -1 if there are fewer than k officers
        print(order[query[1] - 1] if query[1] <= len(order) else -1)
    
    return order

