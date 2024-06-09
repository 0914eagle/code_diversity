
def get_max_area(points):
    max_area = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                for l in range(k+1, len(points)):
                    area = get_area(points[i], points[j], points[k], points[l])
                    if area > max_area:
                        max_area = area
    return max_area

def get_area(p1, p2, p3, p4):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p4[1]) + p3[0] * (p4[1] - p1[1]) + p4[0] * (p1[1] - p2[1])) / 2)

points = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(get_max_area(points))

