
def get_max_area(special_points):
    max_area = 0
    for i in range(len(special_points)):
        for j in range(i+1, len(special_points)):
            for k in range(j+1, len(special_points)):
                for l in range(k+1, len(special_points)):
                    area = get_area(special_points[i], special_points[j], special_points[k], special_points[l])
                    if area > max_area:
                        max_area = area
    return max_area

def get_area(p1, p2, p3, p4):
    return abs((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p4[1]) + p3[0] * (p4[1] - p1[1]) + p4[0] * (p1[1] - p2[1])) / 2)

special_points = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    special_points.append((x, y))

print(get_max_area(special_points))

