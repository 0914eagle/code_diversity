
def get_center_coordinates(coordinates):
    x_coords = [x for x, y, z in coordinates]
    y_coords = [y for x, y, z in coordinates]
    x_center = sum(x_coords) / len(x_coords)
    y_center = sum(y_coords) / len(y_coords)
    return x_center, y_center

def get_height(coordinates):
    heights = [z for x, y, z in coordinates]
    return max(heights)

def main():
    coordinates = []
    for _ in range(int(input())):
        coordinates.append(list(map(int, input().split())))
    x_center, y_center = get_center_coordinates(coordinates)
    height = get_height(coordinates)
    print(f"{x_center} {y_center} {height}")

if __name__ == '__main__':
    main()

