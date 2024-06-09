
def get_center_coordinates(x_coords, y_coords):
    x_sum = sum(x_coords)
    y_sum = sum(y_coords)
    return x_sum // len(x_coords), y_sum // len(y_coords)

def get_height(x_coords, y_coords, h_coords):
    return max(max(h_coords) - abs(x_coords[0] - x_coords[1]) - abs(y_coords[0] - y_coords[1]), 0)

def main():
    n = int(input())
    x_coords = []
    y_coords = []
    h_coords = []
    for i in range(n):
        x, y, h = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
        h_coords.append(h)
    center_x, center_y = get_center_coordinates(x_coords, y_coords)
    height = get_height(x_coords, y_coords, h_coords)
    print(center_x, center_y, height)

if __name__ == '__main__':
    main()

