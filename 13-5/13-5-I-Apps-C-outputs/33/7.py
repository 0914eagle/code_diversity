
def f1(n, k, vertices):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += (vertices[i][0] * vertices[i-1][1]) - (vertices[i][1] * vertices[i-1][0])
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

def f2(n, k, vertices):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += (vertices[i][0] * vertices[i-1][1]) - (vertices[i][1] * vertices[i-1][0])
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    # Calculate the number of maps that cover the entire canyon
    num_maps = int(area / (side_length ** 2))

    return round(side_length, 2)

if __name__ == '__main__':
    n, k = map(int, input().split())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append([x, y])
    print(f1(n, k, vertices))
    print(f2(n, k, vertices))

