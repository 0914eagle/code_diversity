
def get_max_grade(n, k, a, edges):
    # Initialize a dictionary to store the minimum time required to reach each node
    min_time = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a dictionary to store the neighbors of each node
    neighbors = {i: [] for i in range(1, n+1)}
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    # Initialize a queue to do a BFS traversal of the tree
    queue = [1]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for neighbor in neighbors[node]:
            if neighbor not in visited:
                queue.append(neighbor)
        # Update the minimum time required to reach each node in the traversal
        for node in visited:
            min_time[node] = min(min_time[node], min_time[node-1] + a[node-1])
    # Return the maximum grade that Jacob can get
    return max(min_time[i] for i in range(1, k+1))

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(get_max_grade(n, k, a, edges))

if __name__ == '__main__':
    main()

