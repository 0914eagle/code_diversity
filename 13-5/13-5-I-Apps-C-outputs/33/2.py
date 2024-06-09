
def f1(n, k):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += (x[i] * y[(i+1)%n]) - (x[(i+1)%n] * y[i])
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

def f2(n, k):
    # Calculate the area of the polygon
    area = 0
    for i in range(n):
        area += (x[i] * y[(i+1)%n]) - (x[(i+1)%n] * y[i])
    area = abs(area) / 2

    # Calculate the side length of the square maps
    side_length = (area / k) ** 0.5

    return round(side_length, 2)

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    print(f1(n, k))
    print(f2(n, k))

