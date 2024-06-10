
def get_triangle_coordinates(n, m, k):
    for x1 in range(n+1):
        for y1 in range(m+1):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    for x3 in range(x2+1, n+1):
                        for y3 in range(y2+1, m+1):
                            if x1 + x2 + x3 == n and y1 + y2 + y3 == m:
                                return [x1, y1, x2, y2, x3, y3]
    return "NO"

def main():
    n, m, k = map(int, input().split())
    coordinates = get_triangle_coordinates(n, m, k)
    if coordinates == "NO":
        print("NO")
    else:
        print("YES")
        for i in range(3):
            print(coordinates[i*2], coordinates[i*2+1])

if __name__ == '__main__':
    main()

