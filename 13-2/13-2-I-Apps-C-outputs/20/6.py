
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish_count = [[0] * c for _ in range(r)]
    
    # Initialize a queue to store the points to visit
    queue = [(x0, y0)]
    
    # Loop through the points in the queue
    while queue:
        x, y = queue.pop(0)
        
        # Check if the current point is within the time limit
        if times[x][y] <= l:
            # Increment the number of fish at the current point
            fish_count[x][y] += 1
            
            # Add the neighboring points to the queue
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c:
                    queue.append((nx, ny))
    
    # Return the maximum number of fish caught
    return max(sum(x) for x in fish_count)

def f2(...):
    ...

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = [list(map(int, input().split())) for _ in range(r)]
    print(f1(r, c, k, l, x0, y0, times))

