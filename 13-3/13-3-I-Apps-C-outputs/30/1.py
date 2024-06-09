
def f1(n, x_n, y_n, s, x_s, y_s):
    # find the convex hull of the Nazi troops' positions
    hull = []
    hull.append((x_n[0], y_n[0]))
    for i in range(1, n):
        while len(hull) > 1 and not is_left(hull[-2], hull[-1], (x_n[i], y_n[i])):
            hull.pop()
        hull.append((x_n[i], y_n[i]))
    
    # check which castles are in danger
    in_danger = 0
    for i in range(s):
        x, y = x_s[i], y_s[i]
        j = 0
        while j < len(hull) - 1 and not is_left(hull[j], hull[j+1], (x, y)):
            j += 1
        if j == len(hull) - 1:
            continue
        in_danger += 1
    
    return in_danger

def is_left(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

if __name__ == '__main__':
    n = int(input())
    x_n = []
    y_n = []
    for i in range(n):
        x, y = map(int, input().split())
        x_n.append(x)
        y_n.append(y)
    s = int(input())
    x_s = []
    y_s = []
    for i in range(s):
        x, y = map(int, input().split())
        x_s.append(x)
        y_s.append(y)
    print(f1(n, x_n, y_n, s, x_s, y_s))

