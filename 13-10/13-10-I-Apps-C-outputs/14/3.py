
def max_independent_set(n, edges):
    # Initialize a set to store the independent set
    independent_set = set()
    
    # Iterate through the edges
    for edge in edges:
        # If the edge is not part of the independent set, add it to the set
        if edge[0] not in independent_set and edge[1] not in independent_set:
            independent_set.add(edge[0])
            independent_set.add(edge[1])
    
    # Return the size of the independent set
    return len(independent_set)

def main():
    # Read the number of vertices and edges from stdin
    n, m = map(int, input().split())
    
    # Read the edges from stdin
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    
    # Call the max_independent_set function and print the result
    print(max_independent_set(n, edges))

if __name__ == '__main__':
    main()

