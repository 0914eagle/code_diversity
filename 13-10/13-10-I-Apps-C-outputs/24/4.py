
def get_min_wolves_to_remove(graph, pigs):
    # Initialize a set to keep track of the vertices that are safe for the pigs to escape
    safe_vertices = set()
    
    # Iterate through each pig and find the vertices that are safe for them to escape
    for pig in pigs:
        safe_vertices.add(pig)
        for neighbor in graph[pig]:
            if neighbor not in safe_vertices:
                safe_vertices.add(neighbor)
    
    # Return the number of wolves that need to be removed
    return len(graph) - len(safe_vertices)

def main():
    # Read the input data
    V, P = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(V - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    
    # Call the get_min_wolves_to_remove function and print the result
    print(get_min_wolves_to_remove(graph, pigs))

if __name__ == '__main__':
    main()

