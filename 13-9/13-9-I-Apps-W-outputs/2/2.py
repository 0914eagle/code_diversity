
def get_triangle_points(n, m, k):
    for x1 in range(n+1):
        for y1 in range(m+1):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    x3 = n-x1-x2
                    y3 = m-y1-y2
                    if x3 >= 0 and y3 >= 0 and x1*y2+x2*y3+x3*y1 == k:
                        return (x1, y1), (x2, y2), (x3, y3)
    return None

def main():
    n, m, k = map(int, input().split())
    points = get_triangle_points(n, m, k)
    if points is None:
        print("NO")
    else:
        print("YES")
        print(points[0])
        print(points[1])
        print(points[2])

if __name__ == '__main__':
    main()

