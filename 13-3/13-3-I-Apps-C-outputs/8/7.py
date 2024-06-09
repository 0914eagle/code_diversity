
def f1(n, m, pairs):
    # convert the pairs into a graph
    graph = [[] for _ in range(n + 1)]
    for p, q, c in pairs:
        graph[p].append((q, c))
        graph[q].append((p, c))
    
    # find the minimum spanning tree
    parent = [0] * (n + 1)
    cost = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i], cost[i] = min((j, c) for j, c in graph[i] if j not in parent)
    
    # calculate the total cost
    total_cost = 0
    for i in range(1, n + 1):
        if parent[i] != 0:
            total_cost += cost[i]
    
    return total_cost

def f2(n, m, pairs):
    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # find the minimum spanning tree
    parent = [-1] * n
    cost = [0] * n
    for i in range(n):
        parent[i], cost[i] = min((j, c) for j, c in graph[i] if j not in parent)
    
    # calculate the total cost
    total_cost = 0
    for i in range(n):
        if parent[i] != -1:
            total_cost += cost[i]
    
    return total_cost

if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        p, q, c = map(int, input().split())
        pairs.append((p, q, c))
    print(f1(n, m, pairs))
    print(f2(n, m, pairs))

