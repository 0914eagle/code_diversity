
def solve(N, C, a, b, Q, requirements_changes):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {}
    for i in range(N):
        colored_paintings[i+1] = 0
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the requirements changes
    for P, a_P, b_P in requirements_changes:
        # If the client has purchased at least one colored painting, remove them from the set of clients who have not purchased any colored paintings
        if P in colored_clients:
            colored_clients.remove(P)
        # If the client has purchased at least one black and white painting, add them to the set of clients who have not purchased any colored paintings
        if b_P > 0:
            colored_clients.add(P)
        # Update the number of colored paintings purchased by the client
        colored_paintings[P] = a_P
    
    # Return the number of different purchases modulo 10007
    return len(colored_clients) % 10007

