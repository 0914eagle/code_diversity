
def get_min_carbon_dioxide(n, m, pairs):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # Use a union-find data structure to find the minimum spanning tree
    parent = [i for i in range(n)]
    rank = [0] * n
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    total_carbon_dioxide = 0
    for i in range(n):
        for j, c in graph[i]:
            if find(i) != find(j):
                union(i, j)
                total_carbon_dioxide += c
    
    # Check if the graph is connected
    if len(set(find(i) for i in range(n))) == 1:
        return total_carbon_dioxide
    else:
        return "impossible"

def main():
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        p, q, c = map(int, input().split())
        pairs.append((p, q, c))
    print(get_min_carbon_dioxide(n, m, pairs))

if __name__ == '__main__':
    main()

