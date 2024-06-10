
def get_max_independent_set_size(n, edges):
    # Initialize a set to store the independent set
    independent_set = set()
    # Iterate through the edges
    for edge in edges:
        # If the edge is not in the independent set, add it
        if edge[0] not in independent_set and edge[1] not in independent_set:
            independent_set.add(edge[0])
            independent_set.add(edge[1])
    # Return the size of the independent set
    return len(independent_set)

def main():
    # Read the number of vertices and edges
    n, m = map(int, input().split())
    # Read the edges
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    # Find the maximum independent set size
    max_independent_set_size = get_max_independent_set_size(n, edges)
    # Print the result
    print(max_independent_set_size)

if __name__ == '__main__':
    main()

