
def solve(N, C, a, b, Q, P, a_new, b_new):
    # Initialize a dictionary to store the number of colored and black and white paintings for each client
    paintings = {}
    for i in range(N):
        paintings[i+1] = [a[i], b[i]]
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the requirement changes
    for i in range(Q):
        # Update the number of colored and black and white paintings for the client who changed their requirements
        paintings[P[i]] = [a_new[i], b_new[i]]
        
        # Check if the client has purchased at least one colored painting
        if paintings[P[i]][0] > 0:
            colored_clients.add(P[i])
    
    # Count the number of different purchases
    num_purchases = 0
    for client in paintings:
        # If the client has purchased at least one colored painting, add the number of colored paintings they want
        if client in colored_clients:
            num_purchases += paintings[client][0]
        # If the client has not purchased any colored paintings, add the number of black and white paintings they want
        else:
            num_purchases += paintings[client][1]
    
    # Return the number of different purchases modulo 10007
    return num_purchases % 10007

