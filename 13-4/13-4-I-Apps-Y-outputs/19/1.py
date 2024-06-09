
def get_center_coordinates(coordinates):
    x_coords = [x for x, _, _ in coordinates]
    y_coords = [y for _, y, _ in coordinates]
    x_center = sum(x_coords) / len(x_coords)
    y_center = sum(y_coords) / len(y_coords)
    return x_center, y_center

def get_height(coordinates):
    heights = [h for _, _, h in coordinates]
    return max(heights)

def main():
    coordinates = []
    for _ in range(int(input())):
        coordinates.append(tuple(map(int, input().split())))
    x_center, y_center = get_center_coordinates(coordinates)
    height = get_height(coordinates)
    print(f"{x_center} {y_center} {height}")

if __name__ == '__main__':
    main()

