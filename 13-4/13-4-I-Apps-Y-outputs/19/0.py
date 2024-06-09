
def get_center_coordinates(coordinates):
    x_coords = [x for x, _, _ in coordinates]
    y_coords = [y for _, y, _ in coordinates]
    x_center = sum(x_coords) / len(x_coords)
    y_center = sum(y_coords) / len(y_coords)
    return (x_center, y_center)

def get_height(coordinates):
    heights = [h for _, _, h in coordinates]
    return max(heights)

def solve(coordinates):
    center_coordinates = get_center_coordinates(coordinates)
    height = get_height(coordinates)
    return center_coordinates + (height,)

if __name__ == '__main__':
    num_coordinates = int(input())
    coordinates = []
    for _ in range(num_coordinates):
        x, y, h = map(int, input().split())
        coordinates.append((x, y, h))
    print(*solve(coordinates))

