
def get_lifelines(n, edges):
    # Initialize a dictionary to store the vertices and their neighbors
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the lifelines
    lifelines = set()

    # Iterate through the vertices and their neighbors
    for vertex, neighbors in neighbors.items():
        # If the vertex has two neighbors, it is a lifeline
        if len(neighbors) == 2:
            lifelines.add(tuple(sorted((vertex, neighbors.pop()))))

    return len(lifelines)

def main():
    n = int(input())
    edges = []

    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))

    print(get_lifelines(n, edges))

if __name__ == '__main__':
    main()

