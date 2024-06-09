
def get_diagonal_intersections(N):
    # Initialize a list to store the vertices of the polygon
    vertices = []

    # Read the vertices of the polygon from the input
    for i in range(N):
        x, y = map(int, input().split())
        vertices.append((x, y))

    # Initialize a set to store the diagonals of the polygon
    diagonals = set()

    # Iterate over the vertices of the polygon
    for i in range(N):
        # Get the current vertex and the next vertex in the polygon
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % N]

        # Get the slope of the line segment connecting the current vertex and the next vertex
        slope = (next_vertex[1] - current_vertex[1]) / (next_vertex[0] - current_vertex[0])

        # Add the diagonal to the set of diagonals
        diagonals.add(slope)

    # Initialize a counter to store the number of intersections between pairs of diagonals
    intersection_count = 0

    # Iterate over the diagonals of the polygon
    for i in range(N):
        # Get the current diagonal and the next diagonal in the polygon
        current_diagonal = diagonals[i]
        next_diagonal = diagonals[(i + 1) % N]

        # Check if the current diagonal and the next diagonal intersect
        if current_diagonal != next_diagonal:
            intersection_count += 1

    # Return the number of intersections between pairs of diagonals
    return intersection_count

def main():
    # Read the number of vertices from the input
    N = int(input())

    # Call the function to get the number of intersections between pairs of diagonals
    intersection_count = get_diagonal_intersections(N)

    # Print the number of intersections
    print(intersection_count)

if __name__ == '__main__':
    main()

