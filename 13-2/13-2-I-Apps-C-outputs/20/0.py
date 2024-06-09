
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish = [[0] * c for _ in range(r)]
    
    # Initialize a queue to store the points to visit
    queue = [(x0, y0)]
    
    # Initialize a set to store the points that have been visited
    visited = set()
    
    # Loop through the queue until it is empty
    while queue:
        # Get the current point from the queue
        x, y = queue.pop(0)
        
        # If the current point has not been visited before, mark it as visited and add it to the set
        if (x, y) not in visited:
            visited.add((x, y))
            
            # Update the number of fish at the current point
            fish[x][y] += 1
            
            # Add the neighboring points to the queue
            if x > 0:
                queue.append((x - 1, y))
            if x < r - 1:
                queue.append((x + 1, y))
            if y > 0:
                queue.append((x, y - 1))
            if y < c - 1:
                queue.append((x, y + 1))
    
    # Return the maximum number of fish that can be caught
    return max(sum(row) for row in fish)

def f2(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish = [[0] * c for _ in range(r)]
    
    # Loop through the times array and update the fish array accordingly
    for i in range(len(times)):
        for j in range(len(times[i])):
            fish[i][j] += times[i][j]
    
    # Return the maximum number of fish that can be caught
    return max(sum(row) for row in fish)

if __name__ == '__main__':
    r, c, k, l = map(int, input().split())
    x0, y0 = map(int, input().split())
    times = []
    for i in range(r):
        times.append(list(map(int, input().split())))
    
    print(f1(r, c, k, l, x0, y0, times))
    print(f2(r, c, k, l, x0, y0, times))

