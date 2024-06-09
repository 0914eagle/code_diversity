
def is_aesthetically_pleasing(points, special_values):
    # Sort the points by their special values in descending order
    points = sorted(points, key=lambda x: x[1] - x[0], reverse=True)
    # Create a dictionary to map each point to its special value
    special_values_map = {point: special_value for point, special_value in zip(points, special_values)}
    # Initialize the current special value to the maximum special value
    current_special_value = special_values[0]
    # Iterate through the points and check if the current special value is greater than or equal to the special value of the current point
    for point in points:
        if current_special_value < special_values_map[point]:
            return False
        current_special_value = special_values_map[point]
    return True

def find_aesthetically_pleasing_numbering(points, special_values):
    # Sort the points by their special values in descending order
    points = sorted(points, key=lambda x: x[1] - x[0], reverse=True)
    # Create a dictionary to map each point to its special value
    special_values_map = {point: special_value for point, special_value in zip(points, special_values)}
    # Initialize the current special value to the maximum special value
    current_special_value = special_values[0]
    # Initialize the numbering of the points
    numbering = [0] * len(points)
    # Iterate through the points and check if the current special value is greater than or equal to the special value of the current point
    for i, point in enumerate(points):
        if current_special_value < special_values_map[point]:
            return None
        numbering[i] = current_special_value
        current_special_value = special_values_map[point]
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
        for point in numbering:
            print(point)
    else:
        print("NO")

if __name__ == '__main__':
    main()

