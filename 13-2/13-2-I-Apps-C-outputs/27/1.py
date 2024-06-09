
def f1(n, k, vertices):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (vertices[i][0] * vertices[i-1][1]) - (vertices[i-1][0] * vertices[i][1])
    total_area = abs(total_area) / 2

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = (map_area / n) ** 0.5

    return round(side_length, 2)

def f2(n, k, vertices):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (vertices[i][0] * vertices[i-1][1]) - (vertices[i-1][0] * vertices[i][1])
    total_area = abs(total_area) / 2

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = (map_area / n) ** 0.5

    return round(side_length, 2)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append([x, y])
    print(f1(n, k, vertices))
    print(f2(n, k, vertices))

