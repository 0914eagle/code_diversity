
def get_max_dominoes(n, m, edges):
    # Initialize a dictionary to store the number of dots on each vertex
    dots = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the number of dots on each vertex
    for edge in edges:
        a, b = edge
        dots[a] += 1
        dots[b] += 1
    
    # Initialize a set to store the unique dot combinations
    unique_dots = set()
    
    # Iterate over the vertices and add the dot combinations to the set
    for vertex in range(1, n + 1):
        unique_dots.add(tuple(sorted((dots[vertex], 6 - dots[vertex]))))
    
    # Return the maximum number of dominoes that can be placed on the edges
    return len(unique_dots)

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    print(get_max_dominoes(n, m, edges))

if __name__ == '__main__':
    main()

