
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish = [[0] * c for _ in range(r)]
    
    # Initialize a set to store the points that have fish
    points = set()
    
    # Iterate through the input times and update the fish array and points set
    for i in range(r):
        for j in range(c):
            if times[i][j] <= l:
                fish[i][j] = 1
                points.add((i, j))
    
    # Initialize a queue to store the points to visit
    queue = [(x0, y0)]
    
    # Initialize a set to store the visited points
    visited = set()
    
    # Iterate through the queue and visit each point
    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        
        # Check if the point has fish and has not been visited before
        if fish[x][y] and (x, y) not in visited:
            # Add the point to the set of points with fish
            points.add((x, y))
            
            # Add the neighboring points to the queue
            if x > 0:
                queue.append((x - 1, y))
            if x < r - 1:
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if y < c - 1:
                queue.append((x, y + 1))
    
    # Return the number of points with fish
    return len(points)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = []
    for i in range(r):
        times.append(list(map(int, input().split())))
    print(f1(r, c, k, l, x0, y0, times))

