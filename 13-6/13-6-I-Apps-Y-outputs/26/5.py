
def get_cost(n, edges, values):
    # Initialize the cost as 0
    cost = 0
    
    # Loop through each edge and calculate the distance between the vertices
    for edge in edges:
        cost += values[edge[0] - 1] * (n - 1)
    
    return cost

def main():
    # Read the number of vertices and edges
    n, m = map(int, input().split())
    
    # Read the values of the vertices
    values = list(map(int, input().split()))
    
    # Read the edges
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    
    # Calculate the cost of the tree
    cost = get_cost(n, edges, values)
    
    # Print the cost
    print(cost)

if __name__ == '__main__':
    main()

