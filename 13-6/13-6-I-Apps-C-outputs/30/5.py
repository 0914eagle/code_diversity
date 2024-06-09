
def f1(n, m, q):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a-1].append((b-1, w))
        graph[b-1].append((a-1, w))
    
    # Find the shortest path between every pair of nodes using BFS
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    queue = [(0, i) for i in range(n)]
    while queue:
        cost, node = queue.pop(0)
        for neighbor, weight in graph[node]:
            if dist[node][neighbor] > cost + weight:
                dist[node][neighbor] = cost + weight
                queue.append((cost + weight, neighbor))
    
    # Return the shortest distance between any pair of nodes
    return dist

def f2(s, t, q):
    # Initialize the cost of sending a crystal from s to t as 0
    cost = 0
    
    # Loop through each day
    for _ in range(q):
        # Read the input for the current day
        s, t = map(int, input().split())
        
        # Calculate the cost of sending a crystal from s to t for the current day
        cost = f1(n, m, q)[s-1][t-1]
        
        # Print the cost of sending a crystal from s to t for the current day
        print(cost)

if __name__ == '__main__':
    n, m = map(int, input().split())
    q = int(input())
    f2(s, t, q)

