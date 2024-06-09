
def solve(A, B):
    # Find the convex hull of polygon B
    hull = []
    for point in B:
        if len(hull) == 0 or point[0] < hull[0][0] or (point[0] == hull[0][0] and point[1] < hull[0][1]):
            hull.insert(0, point)
    for point in B:
        if len(hull) == 0 or point[0] > hull[-1][0] or (point[0] == hull[-1][0] and point[1] > hull[-1][1]):
            hull.append(point)
    for i in range(1, len(B) - 1):
        for j in range(i + 1, len(B)):
            if B[i][0] == B[j][0] and B[i][1] == B[j][1]:
                continue
            line = [B[i], B[j]]
            hull_index = 0
            while hull_index < len(hull) - 1 and do_lines_intersect(line, [hull[hull_index], hull[hull_index + 1]]):
                hull_index += 1
            if hull_index == len(hull) - 1:
                hull.pop()
            else:
                hull.insert(hull_index, line[0])
                hull.insert(hull_index + 1, line[1])
    # Find the minimum cost to cut polygon B out of polygon A
    min_cost = 0
    for line in hull:
        cost = 0
        for point in A:
            if do_points_strictly_inside_line(point, line):
                cost += distance(point, line)
        min_cost += cost
    return min_cost

def do_lines_intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    return (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4) != 0 and (x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3) >= 0 and (x1 - x4) * (y2 - y4) - (y1 - y4) * (x2 - x4) >= 0

def do_points_strictly_inside_line(point, line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    x3, y3 = point
    return (x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3) > 0

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

