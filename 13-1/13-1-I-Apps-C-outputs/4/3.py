
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
    
    # Initialize a set to store the clients who have purchased at least one black and white painting
    black_and_white_clients = set()
    
    # Loop through the clients and update the number of black and white paintings purchased by each client
    for i in range(N):
        if b[i] > 0:
            black_and_white_clients.add(i+1)
    
    # If the number of black and white clients is equal to the number of colored clients, return 1
    if len(black_and_white_clients) == len(colored_clients):
        return 1
    
    # If the number of black and white clients is greater than the number of colored clients, return 0
    if len(black_and_white_clients) > len(colored_clients):
        return 0
    
    # If the number of black and white clients is less than the number of colored clients, return the number of different purchases
    return len(colored_clients) - len(black_and_white_clients)

def f2(N, C, a, b, Q, changes):
    # Initialize a list to store the number of different purchases for each requirement change
    purchases = []
    
    # Loop through the requirement changes and update the number of colored paintings purchased by each client
    for i in range(Q):
        client, a_new, b_new = changes[i]
        a[client-1] = a_new
        b[client-1] = b_new
        purchases.append(f1(N, C, a, b))
    
    # Return the list of number of different purchases
    return purchases

if __name__ == '__main__':
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    changes = []
    for i in range(Q):
        client, a_new, b_new = map(int, input().split())
        changes.append((client, a_new, b_new))
    print(*f2(N, C, a, b, Q, changes), sep='\n')

