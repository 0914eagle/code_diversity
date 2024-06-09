
def solve(n, q, x, y, a, b):
    # convert the coordinates to a set of points
    points = set()
    for i in range(n):
        points.add((x[i], y[i]))
    
    # find the minimum side length of a square that contains all points
    side_length = 0
    for i in range(n):
        for j in range(i+1, n):
            if (x[i] == x[j] and y[i] == y[j]) or (x[i] == x[j] and abs(y[i] - y[j]) == 1) or (y[i] == y[j] and abs(x[i] - x[j]) == 1):
                side_length = max(side_length, abs(x[i] - x[j]) + 1)
    
    # find the minimum side length of a square that contains all points and ignores at most one point
    side_length_ignoring_one = 0
    for i in range(n):
        for j in range(i+1, n):
            if (x[i] == x[j] and y[i] == y[j]) or (x[i] == x[j] and abs(y[i] - y[j]) == 1) or (y[i] == y[j] and abs(x[i] - x[j]) == 1):
                side_length_ignoring_one = max(side_length_ignoring_one, abs(x[i] - x[j]) + 1)
    
    # return the minimum side length
    return side_length_ignoring_one

