
def solve(N, C, a, b, Q, requirements):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {i: 0 for i in range(1, N+1)}
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    # Initialize a variable to store the total number of different purchases
    total_purchases = 0
    
    for i in range(Q):
        # Unpack the requirement changes for the current iteration
        P, a_P, b_P = requirements[i]
        # Update the number of colored paintings purchased by the current client
        colored_paintings[P] = a_P
        # If the current client has purchased at least one colored painting, add them to the set of colored clients
        if a_P > 0:
            colored_clients.add(P)
        # If the number of colored clients is less than or equal to C, add the number of different purchases
        if len(colored_clients) <= C:
            total_purchases += 1
    
    return total_purchases % 10007

