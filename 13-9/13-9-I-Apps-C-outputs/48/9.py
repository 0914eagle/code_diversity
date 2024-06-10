
def get_min_wolves_to_remove(graph, pigs):
    # Initialize a set to store the vertices that are not leaves
    non_leaves = set()
    
    # Iterate over the graph and find all the vertices that are not leaves
    for vertex in graph:
        if len(graph[vertex]) > 1:
            non_leaves.add(vertex)
    
    # Initialize a set to store the vertices that are occupied by pigs
    pig_vertices = set(pigs)
    
    # Initialize a set to store the vertices that are occupied by wolves
    wolf_vertices = set()
    
    # Iterate over the graph and find all the vertices that are occupied by wolves
    for vertex in graph:
        if vertex not in pig_vertices:
            wolf_vertices.add(vertex)
    
    # Initialize a variable to store the minimum number of wolves to remove
    min_wolves = 0
    
    # Iterate over the pig vertices and check if they can escape
    for pig_vertex in pig_vertices:
        # If the pig vertex is not a leaf vertex and is not occupied by a wolf, then the pig cannot escape
        if pig_vertex in non_leaves and pig_vertex not in wolf_vertices:
            min_wolves += 1
    
    return min_wolves

def main():
    # Read the input graph and pig positions from stdin
    num_vertices, num_pigs = map(int, input().split())
    graph = {}
    for _ in range(num_vertices - 1):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    
    # Find the minimum number of wolves to remove such that every pig can escape
    min_wolves = get_min_wolves_to_remove(graph, pigs)
    
    # Print the minimum number of wolves to remove
    print(min_wolves)

if __name__ == '__main__':
    main()

