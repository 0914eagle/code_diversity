
def get_min_carbon_dioxide(n, m, pairs):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the pairs of friends
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))

    # Use a minimum spanning tree algorithm to find the minimum cost of connecting all nodes
    cost = 0
    visited = set()
    queue = [(0, 0)]
    while queue:
        node, cost_so_far = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        cost += cost_so_far
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, cost))

    # Return the minimum cost
    return cost

def main():
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        p, q, c = map(int, input().split())
        pairs.append((p, q, c))
    print(get_min_carbon_dioxide(n, m, pairs))

if __name__ == '__main__':
    main()

