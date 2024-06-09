
def f1(N, C, a, b):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {}
    for i in range(N):
        colored_paintings[i+1] = 0
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the clients and update the number of colored paintings purchased by each client
    for i in range(N):
        if a[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Initialize a set to store the combinations of colored paintings purchased by each client
    combinations = set()
    
    # Loop through the clients and add the combinations of colored paintings purchased by each client to the set
    for i in range(N):
        if colored_paintings[i+1] > 0:
            combinations.add(colored_paintings[i+1])
    
    # Return the number of combinations modulo 10007
    return len(combinations) % 10007

def f2(N, C, a, b, Q, P, a_new, b_new):
    # Initialize a dictionary to store the number of colored paintings purchased by each client
    colored_paintings = {}
    for i in range(N):
        colored_paintings[i+1] = 0
    
    # Initialize a set to store the clients who have purchased at least one colored painting
    colored_clients = set()
    
    # Loop through the clients and update the number of colored paintings purchased by each client
    for i in range(N):
        if a[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Initialize a set to store the combinations of colored paintings purchased by each client
    combinations = set()
    
    # Loop through the clients and add the combinations of colored paintings purchased by each client to the set
    for i in range(N):
        if colored_paintings[i+1] > 0:
            combinations.add(colored_paintings[i+1])
    
    # Update the number of colored paintings purchased by the client with label P
    colored_paintings[P] = a_new
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Add the new combination of colored paintings purchased by the client with label P to the set
    combinations.add(a_new)
    
    # Return the number of combinations modulo 10007
    return len(combinations) % 10007

if __name__ == '__main__':
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    
    for i in range(Q):
        P, a_new, b_new = map(int, input().split())
        print(f2(N, C, a, b, Q, P, a_new, b_new))

