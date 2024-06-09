
def f1(n, k):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = (map_area / (n * 2)) ** 0.5

    return side_length

def f2(n, k):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = (map_area / (n * 2)) ** 0.5

    return side_length

if __name__ == '__main__':
    n, k = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    print(f1(n, k))
    print(f2(n, k))

