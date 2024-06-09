
def get_maximum_gold(n, m, roads, gold):
    # Initialize a graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize a visited array and a parent array
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    
    # Initialize the maximum gold to 0
    max_gold = 0
    
    # Iterate through all the vertices except the bandit's home
    for vertex in range(2, n + 1):
        # If the vertex is not visited, explore it
        if not visited[vertex]:
            # Explore the vertex and its neighbors
            explore_vertex(graph, visited, parent, vertex, gold)
            # Add the gold collected by the bandits to the maximum gold
            max_gold += gold[vertex]
    
    # Return the maximum gold collected by the bandits
    return max_gold

def explore_vertex(graph, visited, parent, vertex, gold):
    # Mark the vertex as visited
    visited[vertex] = True
    # Iterate through the neighbors of the vertex
    for neighbor in graph[vertex]:
        # If the neighbor is not visited, explore it
        if not visited[neighbor]:
            # Explore the neighbor and its neighbors
            explore_vertex(graph, visited, parent, neighbor, gold)
            # Add the gold collected by the bandits to the maximum gold
            gold[vertex] += gold[neighbor]
            # Set the parent of the neighbor to the current vertex
            parent[neighbor] = vertex

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    gold = list(map(int, input().split()))
    print(get_maximum_gold(n, m, roads, gold))

