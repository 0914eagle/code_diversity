
def get_triangle_coordinates(n, m, k):
    for x1 in range(n+1):
        for y1 in range(m+1):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    x3 = n - x1 - x2
                    y3 = m - y1 - y2
                    if x3 >= 0 and y3 >= 0 and x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2) == k:
                        return [x1, y1, x2, y2, x3, y3]
    return []

def main():
    n, m, k = map(int, input().split())
    coordinates = get_triangle_coordinates(n, m, k)
    if coordinates:
        print("YES")
        for x, y in zip(coordinates, coordinates[1:]):
            print(x, y)
    else:
        print("NO")

if __name__ == '__main__':
    main()

