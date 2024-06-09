
def f1(colors):
    # Initialize variables
    num_operations = 0
    num_points = len(colors)
    points_to_delete = []

    # Iterate through the points and find the points that need to be deleted
    for i in range(num_points):
        if i > 0 and i < num_points - 1:
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                points_to_delete.append(i)
        elif i == 0 and colors[i] != colors[i + 1]:
            points_to_delete.append(i)
        elif i == num_points - 1 and colors[i] != colors[i - 1]:
            points_to_delete.append(i)

    # Delete the points
    for point in points_to_delete:
        colors = colors[:point] + colors[point + 1:]
        num_operations += 1

    return num_operations

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    colors = input()
    print(f1(colors))

