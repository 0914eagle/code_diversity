
def count_lifelines(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {}
    for edge in edges:
        # Add the neighbors of each vertex to the dictionary
        neighbors[edge[0]] = neighbors.get(edge[0], []) + [edge[1]]
        neighbors[edge[1]] = neighbors.get(edge[1], []) + [edge[0]]
    
    # Initialize a set to store the lifelines
    lifelines = set()
    for vertex in range(1, n + 1):
        # Iterate over the neighbors of each vertex
        for neighbor in neighbors[vertex]:
            # If the neighbor is smaller than the vertex, add the edge to the set of lifelines
            if neighbor < vertex:
                lifelines.add((vertex, neighbor))
    
    return len(lifelines)

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    print(count_lifelines(n, edges))

if __name__ == '__main__':
    main()

