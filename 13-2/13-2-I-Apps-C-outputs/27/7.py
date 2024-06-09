
def f1(n, k, polygon):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += polygon[i][0] * polygon[i-1][1] - polygon[i-1][0] * polygon[i][1]
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

def f2(n, k, polygon):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += polygon[i][0] * polygon[i-1][1] - polygon[i-1][0] * polygon[i][1]
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    # Calculate the minimum area of the maps
    min_area = side_length ** 2

    return round(min_area, 2)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    polygon = []
    for i in range(n):
        x, y = map(int, input().split())
        polygon.append([x, y])
    print(f1(n, k, polygon))
    print(f2(n, k, polygon))

