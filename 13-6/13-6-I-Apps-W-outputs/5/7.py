
def triangulate_polygon(n):
    # Initialize a list to store the weights of all triangulations
    weights = []
    
    # Iterate over all possible ways to divide the polygon into triangles
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Calculate the weight of the current triangulation
                weight = i * j * k
                # Add the weight to the list of weights
                weights.append(weight)
    
    # Return the minimum weight among all triangulations
    return min(weights)

def main():
    # Read the number of vertices in the polygon from stdin
    n = int(input())
    # Calculate the minimum weight of the polygon
    weight = triangulate_polygon(n)
    # Print the minimum weight
    print(weight)

if __name__ == '__main__':
    main()

