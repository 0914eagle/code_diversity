
def get_input():
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    return N, points

def is_right_triangle(p1, p2, p3):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 == (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2

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

