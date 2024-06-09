
def get_center_coordinates(x_coordinates, y_coordinates):
    x_sum = sum(x_coordinates)
    y_sum = sum(y_coordinates)
    center_x = x_sum // len(x_coordinates)
    center_y = y_sum // len(y_coordinates)
    return center_x, center_y

def get_height(x_coordinates, y_coordinates, heights):
    height = max(heights)
    return height

def main():
    num_points = int(input())
    x_coordinates = []
    y_coordinates = []
    heights = []
    for i in range(num_points):
        x, y, h = map(int, input().split())
        x_coordinates.append(x)
        y_coordinates.append(y)
        heights.append(h)
    center_x, center_y = get_center_coordinates(x_coordinates, y_coordinates)
    height = get_height(x_coordinates, y_coordinates, heights)
    print(center_x, center_y, height)

if __name__ == '__main__':
    main()

