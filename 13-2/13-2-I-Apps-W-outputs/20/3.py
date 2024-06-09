
def f1(colors):
    # Initialize variables
    num_operations = 0
    num_points = len(colors)
    points_to_delete = set()

    # Iterate through the colors
    for i in range(num_points):
        # If the current point has a neighbor of a different color, add it to the set of points to delete
        if i > 0 and i < num_points - 1 and colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
            points_to_delete.add(i)
    
    # If there are no points to delete, return -1
    if not points_to_delete:
        return -1
    
    # Delete the points and increment the number of operations
    for point in points_to_delete:
        colors.pop(point)
    num_operations += 1
    
    return num_operations

def f2(colors):
    # Initialize variables
    num_operations = 0
    num_points = len(colors)
    points_to_delete = set()

    # Iterate through the colors
    for i in range(num_points):
        # If the current point has a neighbor of a different color, add it to the set of points to delete
        if i > 0 and i < num_points - 1 and colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
            points_to_delete.add(i)
    
    # If there are no points to delete, return -1
    if not points_to_delete:
        return -1
    
    # Delete the points and increment the number of operations
    for point in points_to_delete:
        colors.pop(point)
    num_operations += 1
    
    return num_operations

if __name__ == '__main__':
    colors = input()
    print(f1(colors))
    print(f2(colors))

