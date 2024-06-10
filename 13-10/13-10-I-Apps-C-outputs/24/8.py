
def is_leaf(vertex, graph):
    
    neighbors = graph[vertex]
    return len(neighbors) == 1

def escape_pigs(graph, pig_positions):
    
    # Initialize a set to store the positions of the wolves
    wolf_positions = set()

    # Iterate through the pigs and determine if they can escape
    for pig in pig_positions:
        if is_leaf(pig, graph):
            continue
        # If the pig is not on a leaf vertex, it cannot escape
        return -1

    # If all pigs can escape, return the number of wolves to remove
    return len(wolf_positions)

def main():
    # Read the input data
    num_vertices, num_pigs = map(int, input().split())
    graph = [[] for _ in range(num_vertices)]
    for _ in range(num_vertices - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pig_positions = list(map(int, input().split()))

    # Call the escape_pigs function to determine the minimum number of wolves to remove
    result = escape_pigs(graph, pig_positions)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

