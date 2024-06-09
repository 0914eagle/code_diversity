
def solve(n, q, p, queries):
    # Initialize a list to store the order of officers receiving the command
    order = []
    
    # Loop through each query
    for query in queries:
        # Initialize a set to store the indices of officers who have received the command
        received = set()
        
        # Initialize the current officer as the query officer
        current = query[0]
        
        # Loop until the command has been spread to all officers
        while len(order) < n:
            # If the current officer has not received the command yet, add them to the order
            if current not in received:
                order.append(current)
                received.add(current)
            
            # Find the next officer to spread the command to
            next_officer = find_next_officer(current, p, received)
            
            # If there is no next officer, break out of the loop
            if next_officer == -1:
                break
            
            # Set the current officer as the next officer
            current = next_officer
        
        # If the command has been spread to all officers, add the query officer to the order
        if len(order) == n:
            order.append(query[0])
        
        # Print the officer at the required position in the order
        print(order[query[1] - 1] if query[1] <= len(order) else -1)
    
    return order

def find_next_officer(current, p, received):
    # Find the direct subordinates of the current officer
    subordinates = [i for i in range(1, len(p)) if p[i] == current]
    
    # If there are no direct subordinates, return -1
    if not subordinates:
        return -1
    
    # Find the minimum index of the direct subordinates who have not received the command yet
    min_index = min([i for i in subordinates if i not in received])
    
    # Return the minimum index
    return min_index

n, q = map(int, input().split())
p = list(map(int, input().split()))
queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))

order = solve(n, q, p, queries)

