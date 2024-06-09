
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish_count = [[0] * c for _ in range(r)]
    
    # Initialize a set to store the points that have fish
    fish_points = set()
    
    # Loop through each point and update the fish count and fish points
    for i in range(r):
        for j in range(c):
            if times[i][j] <= l:
                fish_count[i][j] = 1
                fish_points.add((i, j))
    
    # Initialize a set to store the points that are reachable from the starting point
    reachable_points = set([(x0, y0)])
    
    # Loop through each point and update the reachable points
    for i in range(r):
        for j in range(c):
            if (i, j) in reachable_points:
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < r and 0 <= y < c and (x, y) not in reachable_points:
                        reachable_points.add((x, y))
    
    # Return the number of fish points that are reachable from the starting point
    return len([point for point in fish_points if point in reachable_points])

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = []
    for i in range(r):
        times.append(list(map(int, input().split())))
    print(f1(r, c, k, l, x0, y0, times))

