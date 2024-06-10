
def get_independent_set_size(n, m, edges):
    # Initialize a set to store the independent set
    independent_set = set()

    # Iterate through the edges
    for edge in edges:
        # If the edge connects two vertices that are already in the independent set, remove them from the independent set
        if edge[0] in independent_set and edge[1] in independent_set:
            independent_set.remove(edge[0])
            independent_set.remove(edge[1])

    # Return the size of the independent set
    return len(independent_set)

def main():
    # Read the input
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    # Find the size of a maximum independent set
    independent_set_size = get_independent_set_size(n, m, edges)

    # Print the result
    print(independent_set_size)

if __name__ == '__main__':
    main()

