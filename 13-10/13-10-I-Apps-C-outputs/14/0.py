
def get_max_independent_set_size(n, m, edges):
    # Initialize a set to store the independent set
    independent_set = set()
    
    # Loop through each edge and add the vertices to the independent set
    for edge in edges:
        independent_set.add(edge[0])
        independent_set.add(edge[1])
    
    # Return the size of the independent set
    return len(independent_set)

def main():
    # Read the input data from stdin
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    
    # Call the function to get the maximum independent set size
    max_independent_set_size = get_max_independent_set_size(n, m, edges)
    
    # Print the output
    print(max_independent_set_size)

if __name__ == '__main__':
    main()

