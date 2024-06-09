
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
        if b[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Otherwise, return the number of different purchases modulo 10007
    return len(set(colored_paintings.values())) % 10007

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
        if b[i] > 0:
            colored_paintings[i+1] += 1
            colored_clients.add(i+1)
    
    # Loop through the requirement changes and update the number of colored paintings purchased and the set of colored clients
    for i in range(Q):
        if P[i] in colored_clients:
            if a_new[i] > 0:
                colored_paintings[P[i]] += 1
            if b_new[i] > 0:
                colored_paintings[P[i]] += 1
        else:
            if a_new[i] > 0:
                colored_paintings[P[i]] += 1
                colored_clients.add(P[i])
            if b_new[i] > 0:
                colored_paintings[P[i]] += 1
                colored_clients.add(P[i])
    
    # If the number of colored clients is less than C, return 0
    if len(colored_clients) < C:
        return 0
    
    # Otherwise, return the number of different purchases modulo 10007
    return len(set(colored_paintings.values())) % 10007

if __name__ == '__main__':
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    P = []
    a_new = []
    b_new = []
    for i in range(Q):
        P.append(int(input()))
        a_new.append(int(input()))
        b_new.append(int(input()))
    print(f1(N, C, a, b))
    for i in range(Q):
        print(f2(N, C, a, b, Q, P[i], a_new[i], b_new[i]))

