
import sys
import itertools

def read_input():
    n, m, k = map(int, input().split())
    capacity = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append((u, v))
    return n, m, k, capacity, connections

def edit_distance(G, k):
    # Initialize the distance matrix with the number of connections
    distance = [[len(G[i]) for i in range(n)] for j in range(n)]
    
    # Iterate through the connections
    for i in range(n):
        for j in range(i+1, n):
            if i != j and distance[i][j] > k:
                return -1
    
    # Iterate through the connections
    for i in range(n):
        for j in range(i+1, n):
            if i != j and distance[i][j] > k:
                return -1
    
    return distance

def is_connected(G, k):
    # Initialize the visited array
    visited = [False] * n
    
    # Iterate through the nodes
    for i in range(n):
        if not visited[i]:
            # Breadth-first search starting from node i
            queue = [i]
            visited[i] = True
            while queue:
                node = queue.pop(0)
                for neighbor in G[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True
    
    # Check if all nodes are visited
    for i in range(n):
        if not visited[i]:
            return False
    
    return True

def main():
    n, m, k, capacity, connections = read_input()
    G = [[] for _ in range(n)]
    for u, v in connections:
        G[u].append(v)
        G[v].append(u)
    if edit_distance(G, k) == -1:
        print("no")
    else:
        print("yes")

if __name__ == '__main__':
    main()

