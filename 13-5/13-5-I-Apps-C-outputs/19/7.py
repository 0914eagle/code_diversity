
def read_points():
    n = int(input())
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def is_right_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1-x2)**2 + (y1-y2)**2 == (x2-x3)**2 + (y2-y3)**2

def count_right_triangles(points):
    n = len(points)
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if is_right_triangle(points[i], points[j], points[k]):
                    count += 1
    return count

if __name__ == '__main__':
    points = read_points()
    print(count_right_triangles(points))

