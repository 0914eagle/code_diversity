
def f1(N, S):
    # find the convex hull of the Nazi troops' positions
    hull = []
    hull.append((0, 0))
    for i in range(N):
        while len(hull) > 1 and not is_left(hull[-2], hull[-1], (N[i][0], N[i][1])):
            hull.pop()
        hull.append((N[i][0], N[i][1]))
    hull.append((0, 0))
    
    # check which castles are in danger
    in_danger = 0
    for i in range(S):
        if is_inside(hull, (S[i][0], S[i][1])):
            in_danger += 1
    
    return in_danger

def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def is_inside(hull, p):
    n = len(hull)
    inside = False
    for i in range(n):
        if is_left(hull[i], hull[(i + 1) % n], p):
            inside = not inside
    return inside

if __name__ == '__main__':
    N = [[0, 1], [3, 7], [4, 5], [6, 5]]
    S = [[1, 4], [1, 6], [2, 3], [2, 5], [3, 5], [3, 6], [4, 8], [5, 4], [6, 3]]
    print(f1(N, S))

