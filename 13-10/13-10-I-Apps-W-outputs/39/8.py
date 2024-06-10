
def get_tree_1(n):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    return graph

def add_edge_1(graph, x, y):
    # Add an edge between x and y
    graph[x].append(y)
    graph[y].append(x)

def find_path_1(graph, a, b, k):
    # Initialize a queue to perform BFS
    queue = [(a, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == b:
            return distance == k
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance+1))
    return False

def solve_queries_1(graph, queries):
    for query in queries:
        x, y, a, b, k = query
        add_edge_1(graph, x, y)
        print("YES" if find_path_1(graph, a, b, k) else "NO")

def main():
    n = int(input())
    graph = get_tree_1(n)
    for _ in range(n-1):
        u, v = map(int, input().split())
        add_edge_1(graph, u, v)
    q = int(input())
    queries = []
    for _ in range(q):
        x, y, a, b, k = map(int, input().split())
        queries.append((x, y, a, b, k))
    solve_queries_1(graph, queries)

if __name__ == '__main__':
    main()

