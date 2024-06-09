
def f1(N, C, a, b):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {}
    for i in range(N):
        colored_paintings[i+1] = 0
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the clients and update the number of colored paintings purchased and the set of colored clients
    for i in range(N):
        if a[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Initialize a variable to store the number of different purchases
    num_purchases = 0
    
    # Loop through the clients and update the number of different purchases
    for i in range(N):
        if a[i] > 0 and b[i] > 0:
            num_purchases += 1
    
    return num_purchases

def f2(N, C, a, b, Q, P, a_new, b_new):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {}
    for i in range(N):
        colored_paintings[i+1] = 0
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the clients and update the number of colored paintings purchased and the set of colored clients
    for i in range(N):
        if a[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Update the number of colored paintings purchased by the client with label P
    colored_paintings[P] += a_new
    
    # If the client with label P has purchased at least one colored painting, add them to the set of colored clients
    if a_new > 0:
        colored_clients.add(P)
    
    # Initialize a variable to store the number of different purchases
    num_purchases = 0
    
    # Loop through the clients and update the number of different purchases
    for i in range(N):
        if a[i] > 0 and b[i] > 0:
            num_purchases += 1
    
    return num_purchases

if __name__ == '__main__':
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    
    for i in range(Q):
        P, a_new, b_new = map(int, input().split())
        print(f2(N, C, a, b, Q, P, a_new, b_new))

