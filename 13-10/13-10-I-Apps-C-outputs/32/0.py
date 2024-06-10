
def is_possible(num_vertices, parent_list, x_list):
    # Initialize the color and weight of each vertex as None
    color = [None] * (num_vertices + 1)
    weight = [None] * (num_vertices + 1)
    
    # Set the color and weight of the root vertex (1)
    color[1] = "white"
    weight[1] = x_list[1]
    
    # Loop through the vertices in the order of their depth in the tree
    for vertex in range(2, num_vertices + 1):
        # Get the parent of the current vertex
        parent = parent_list[vertex]
        
        # If the parent has not been colored yet, color it with the opposite color of the current vertex
        if color[parent] is None:
            color[parent] = "white" if color[vertex] == "black" else "black"
        
        # If the parent has been colored, check if the current vertex has the same color as its parent
        else:
            if color[parent] == color[vertex]:
                return "IMPOSSIBLE"
        
        # Set the weight of the current vertex to be the difference between its X value and the total weight of its descendants
        weight[vertex] = x_list[vertex] - sum(weight[i] for i in range(vertex, num_vertices + 1) if parent_list[i] == vertex)
    
    # If all vertices have been colored and weighted, return "POSSIBLE"
    return "POSSIBLE"

def main():
    num_vertices = int(input())
    parent_list = [int(x) for x in input().split()]
    x_list = [int(x) for x in input().split()]
    print(is_possible(num_vertices, parent_list, x_list))

if __name__ == '__main__':
    main()

