
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
        # and has a special value less than or equal to the current point's special value
        for j in range(len(numbering)):
            if numbering[j] >= point[0] and special_values[j] <= special_value:
                # Assign the current point the next available number in the numbering
                numbering.insert(j + 1, i + 1)
                break

    # If the numbering is aesthetically pleasing, return it
    if len(numbering) == len(points) and all(numbering[i] < numbering[i + 1] for i in range(len(numbering) - 1)):
        return numbering

    # Otherwise, return None
    return None

def main():
    n = int(input())
    points = []
    special_values = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
        special_values.append(y - x)
    numbering = is_aesthetically_pleasing(points, special_values)
    if numbering:
        print("YES")
        for i in numbering:
            print(points[i - 1])
    else:
        print("NO")

if __name__ == '__main__':
    main()

