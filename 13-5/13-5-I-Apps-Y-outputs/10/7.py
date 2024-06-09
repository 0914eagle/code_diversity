
def find_max_edges(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    
    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])
    
    # Initialize a list to store the maximum number of edges in a simple path between any two vertices
    max_edges = [0] * n
    
    # Initialize a list to store the vertices in a simple path between any two vertices
    path = [[] for _ in range(n)]
    
    # Iterate over all pairs of vertices
    for i in range(n):
        for j in range(i + 1, n):
            # If the distance between the two vertices is 1, they are adjacent
            if j - i == 1:
                max_edges[i] += 1
                max_edges[j] += 1
                path[i].append(j)
                path[j].append(i)
            # If the distance between the two vertices is greater than 1, find the shortest path between them
            else:
                queue = [(i, 0)]
                visited = set()
                while queue:
                    vertex, distance = queue.pop(0)
                    if vertex == j:
                        max_edges[i] += distance + 1
                        max_edges[j] += distance + 1
                        path[i].append(j)
                        path[j].append(i)
                        break
                    for neighbor in neighbors[vertex]:
                        if neighbor not in visited:
                            queue.append((neighbor, distance + 1))
                            visited.add(neighbor)
    
    # Find the maximum number of edges in a simple path between any two vertices
    max_edge = max(max_edges)
    
    # Find the vertices that form a simple path with the maximum number of edges
    vertices = []
    for i in range(n):
        if max_edges[i] == max_edge:
            vertices.append(i + 1)
    
    return max_edge, vertices

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    max_edge, vertices = find_max_edges(n, edges)
    print(max_edge)
    print(*vertices)

if __name__ == '__main__':
    main()

