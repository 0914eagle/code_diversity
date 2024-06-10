
def get_lifelines(n, edges):
    # Initialize a dictionary to store the edges
    edge_dict = {}
    for edge in edges:
        # Add the edge to the dictionary
        edge_dict[edge[0]] = edge[1]
    
    # Initialize a set to store the lifelines
    lifelines = set()
    for vertex in range(1, n + 1):
        # If the vertex has an edge, add the edge to the set of lifelines
        if vertex in edge_dict:
            lifelines.add((vertex, edge_dict[vertex]))
    
    return len(lifelines)

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    print(get_lifelines(n, edges))

if __name__ == '__main__':
    main()

