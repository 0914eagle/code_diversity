
def f1(colors):
    # Initialize variables
    num_operations = 0
    num_points = len(colors)
    points_to_delete = set()

    # Iterate through the colors
    for i in range(num_points):
        # Check if the current point has a neighbor of a different color
        if i > 0 and i < num_points - 1 and colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
            # If it does, add it to the set of points to delete
            points_to_delete.add(i)

    # Return the number of operations needed
    return num_operations + 1

def f2(...):
    # Implement the second function here
    pass

if __name__ == '__main__':
    colors = input()
    print(f1(colors))

