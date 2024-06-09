
def solve(N, C, a, b, Q, P, a_new, b_new):
    # Initialize a dictionary to store the number of colored and black and white paintings for each client
    paintings = {i: [0, 0] for i in range(1, N+1)}
    
    # Initialize a set to store the clients who have already purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the requirements changes
    for i in range(Q):
        # Get the client who is changing their requirements
        client = P[i]
        
        # Update the number of colored and black and white paintings for the client
        paintings[client][0] = a_new[i]
        paintings[client][1] = b_new[i]
        
        # If the client has purchased at least one colored painting, add them to the set of colored clients
        if paintings[client][0] > 0:
            colored_clients.add(client)
    
    # Count the number of different purchases
    num_purchases = 0
    for client in paintings:
        # If the client has purchased at least one colored painting, add them to the number of purchases
        if client in colored_clients:
            num_purchases += 1
    
    # Return the number of different purchases modulo 10007
    return num_purchases % 10007

