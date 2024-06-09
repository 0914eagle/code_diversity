
def is_aesthetically_pleasing(points, special_values):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the numbering with the first point
    numbering = [1]

    # Iterate through the remaining points
    for i in range(1, len(points)):
        # Get the current point and its special value
        point = sorted_points[i]
        special_value = special_values[i]

        # Find the first point in the numbering that is greater than or equal to the current point
        for j in range(len(numbering)):
            if point[0] <= sorted_points[j][0] and point[1] <= sorted_points[j][1]:
                # Assign the current point the next available number in the numbering
                numbering.insert(j + 1, i + 1)
                break

    # Check if the special values are satisfied
    for i in range(len(points)):
        if special_values[i] != points[numbering[i] - 1][1] - points[numbering[i] - 1][0]:
            return False

    return True

def find_aesthetically_pleasing_numbering(points, special_values):
    # Initialize the numbering with the first point
    numbering = [1]

    # Iterate through the remaining points
    for i in range(1, len(points)):
        # Get the current point and its special value
        point = points[i]
        special_value = special_values[i]

        # Find the first point in the numbering that is greater than or equal to the current point
        for j in range(len(numbering)):
            if point[0] <= points[numbering[j] - 1][0] and point[1] <= points[numbering[j] - 1][1]:
                # Assign the current point the next available number in the numbering
                numbering.insert(j + 1, i + 1)
                break

    return numbering

def main():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    special_values = list(map(int, input().split()))

    if is_aesthetically_pleasing(points, special_values):
        print("YES")
        numbering = find_aesthetically_pleasing_numbering(points, special_values)
        for i in range(n):
            print(points[numbering[i] - 1][0], points[numbering[i] - 1][1])
    else:
        print("NO")

if __name__ == '__main__':
    main()

