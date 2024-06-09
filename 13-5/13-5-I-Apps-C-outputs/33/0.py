
def f1(n, k):
    # Calculate the total area of the polygon
    total_area = 0
    for i in range(n):
        total_area += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

    # Calculate the area of each map
    map_area = total_area / k

    # Calculate the side length of each map
    side_length = (map_area / n) ** 0.5

    return round(side_length, 2)

def f2(...):
    ...

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(n, k))

