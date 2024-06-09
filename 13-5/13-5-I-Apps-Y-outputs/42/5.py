
def solve(n, q, p, queries):
    # Initialize a list to store the order of officers receiving the command
    order = []
    
    # Iterate over each query
    for query in queries:
        # Initialize a set to store the officers who have received the command
        received = set()
        
        # Initialize the current officer as the query officer
        current = query[0]
        
        # Iterate until the command is spread to all officers
        while len(order) < n:
            # If the current officer has not received the command, add it to the order
            if current not in received:
                order.append(current)
                received.add(current)
            
            # Find the next officer to spread the command to
            next_officer = p[current]
            
            # If the next officer has not received the command, set it as the current officer
            if next_officer not in received:
                current = next_officer
            # If all officers have received the command, break the loop
            else:
                break
        
        # If the order is shorter than the required index, return -1
        if len(order) < query[1]:
            print(-1)
        # Otherwise, return the officer at the required index
        else:
            print(order[query[1] - 1])
    
    return order

