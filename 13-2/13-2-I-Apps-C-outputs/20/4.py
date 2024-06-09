
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish = [[0] * c for _ in range(r)]
    
    # Initialize a 2D array to store the number of fish caught at each point
    caught = [[0] * c for _ in range(r)]
    
    # Set the initial position to the starting point
    x, y = x0, y0
    
    # Loop through each second from 1 to l
    for second in range(1, l + 1):
        # If the current second is a fishing second, update the number of fish at the current position
        if second in times[x][y]:
            fish[x][y] += 1
        
        # If the current second is a catching second, update the number of fish caught at the current position
        if second % k == 0:
            caught[x][y] += fish[x][y]
        
        # Move to the next position in the lake
        x = (x + 1) % r
        y = (y + 1) % c
    
    # Return the maximum number of fish caught
    return max(max(caught))

def f2(...):
    ...

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = []
    for _ in range(r):
        times.append(list(map(int, input().split())))
    print(f1(r, c, k, l, x0, y0, times))

