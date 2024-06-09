
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the minimum number of lines needed to cover all points as infinity
    min_lines = float('inf')

    # Iterate over all possible line combinations
    for i in range(len(sorted_points)):
        for j in range(i+1, len(sorted_points)):
            # Check if the current line combination covers all points
            if set(sorted_points[i:j+1]) == set(points):
                # If it does, update the minimum number of lines needed
                min_lines = min(min_lines, j-i+1)

    # Return YES if the minimum number of lines needed is 2, NO otherwise
    return 'YES' if min_lines == 2 else 'NO'

