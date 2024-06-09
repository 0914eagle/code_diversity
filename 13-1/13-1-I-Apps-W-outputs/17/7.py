
def is_aesthetically_pleasing(points, special_values):
    # Sort the points by their special values in descending order
    points = sorted(points, key=lambda x: x[1] - x[0], reverse=True)
    # Create a dictionary to map each point to its special value
    special_values_map = {point: special_value for point, special_value in zip(points, special_values)}
    # Initialize the current special value to the maximum special value
    current_special_value = special_values[0]
    # Iterate through the points in descending order of their special values
    for point in points:
        # If the current special value is less than the special value of the current point, return False
        if current_special_value < special_values_map[point]:
            return False
        # Otherwise, assign the current special value to the current point and decrease the current special value by 1
        special_values_map[point] = current_special_value
        current_special_value -= 1
    # If all points have been processed and the current special value is 0, return True
    return current_special_value == 0

def find_aesthetically_pleasing_numbering(points, special_values):
    # Initialize the numbering to be the identity mapping
    numbering = {point: i for i, point in enumerate(points, start=1)}
    # Sort the points by their special values in descending order
    points = sorted(points, key=lambda x: x[1] - x[0], reverse=True)
    # Create a dictionary to map each point to its special value
    special_values_map = {point: special_value for point, special_value in zip(points, special_values)}
    # Initialize the current special value to the maximum special value
    current_special_value = special_values[0]
    # Iterate through the points in descending order of their special values
    for point in points:
        # If the current special value is less than the special value of the current point, return False
        if current_special_value < special_values_map[point]:
            return False
        # Otherwise, assign the current special value to the current point and decrease the current special value by 1
        special_values_map[point] = current_special_value
        current_special_value -= 1
        # Update the numbering to reflect the new special value assignment
        numbering[point] = current_special_value + 1
    # If all points have been processed and the current special value is 0, return the numbering
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
        for i in range(1, n + 1):
            print(numbering[(i, i)])
    else:
        print("NO")

if __name__ == '__main__':
    main()

