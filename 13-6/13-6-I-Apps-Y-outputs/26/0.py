
def get_cost(n, a, edges):
    # Initialize the cost as 0
    cost = 0
    
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    # Find the vertex with the maximum value
    max_vertex = a.index(max(a))
    
    # Calculate the cost of the tree
    for i in range(n):
        if i != max_vertex:
            cost += dist(graph, max_vertex, i) * a[i]
    
    return cost

def dist(graph, start, end):
    # Initialize the distance as 0
    distance = 0
    
    # Breadth-first search from the start vertex to the end vertex
    queue = [start]
    visited = [False] * len(graph)
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return distance
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
        distance += 1
    
    # If the end vertex is not found, return -1
    return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(get_cost(n, a, edges))

if __name__ == '__main__':
    main()

