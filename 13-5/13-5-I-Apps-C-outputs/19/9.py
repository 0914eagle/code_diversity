
def get_input():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    return N, points

def is_right_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1-x2)**2 + (y1-y2)**2 == (x3-x2)**2 + (y3-y2)**2

def count_right_triangles(points):
    count = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                if is_right_triangle(points[i], points[j], points[k]):
                    count += 1
    return count

if __name__ == '__main__':
    N, points = get_input()
    print(count_right_triangles(points))

