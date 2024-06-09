
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish = [[0] * c for _ in range(r)]
    
    # Initialize a set to store the points that have fish
    points = set()
    
    # Loop through each row of the input and update the fish array and the points set
    for i in range(r):
        for j in range(c):
            if times[i][j] <= l:
                fish[i][j] = 1
                points.add((i, j))
    
    # Initialize a queue to store the points to visit
    queue = [(x0, y0)]
    
    # Loop until the queue is empty
    while queue:
        x, y = queue.pop(0)
        
        # Check if the current point has fish and if it is within the time limit
        if fish[x][y] and times[x][y] <= l:
            # Catch the fish at the current point
            fish[x][y] = 0
            points.remove((x, y))
            
            # Add the neighbors of the current point to the queue
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in points:
                    queue.append((nx, ny))
    
    # Return the number of points with fish
    return len(points)

def f2(...):
    ...

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = []
    for _ in range(r):
        times.append(list(map(int, input().split())))
    print(f1(r, c, k, l, x0, y0, times))

