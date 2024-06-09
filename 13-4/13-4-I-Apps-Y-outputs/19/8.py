
def get_center_coordinates(coordinates):
    x_coordinates = [x for x, y, z in coordinates]
    y_coordinates = [y for x, y, z in coordinates]
    x_center = sum(x_coordinates) / len(x_coordinates)
    y_center = sum(y_coordinates) / len(y_coordinates)
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
    print(x_center, y_center, height)

if __name__ == '__main__':
    main()

