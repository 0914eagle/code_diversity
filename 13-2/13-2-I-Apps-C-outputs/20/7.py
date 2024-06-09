
def f1(r, c, k, l, x0, y0, times):
    # Initialize a 2D array to store the number of fish at each point
    fish_count = [[0] * c for _ in range(r)]
    
    # Initialize a 2D array to store the maximum number of fish that can be caught at each point
    max_fish = [[0] * c for _ in range(r)]
    
    # Set the initial position to the starting position
    x, y = x0, y0
    
    # Loop through each time step
    for t in range(1, l + 1):
        # If the current position has fish at the current time step, catch them
        if fish_count[x][y] > 0:
            max_fish[x][y] += fish_count[x][y]
        
        # Move to the next position in the direction of the fish
        if t < times[x][y]:
            # If the current position has fish, move to the next position in the direction of the fish
            if fish_count[x][y] > 0:
                if y + 1 < c and fish_count[x][y + 1] > 0:
                    x, y = x, y + 1
                elif x + 1 < r and fish_count[x + 1][y] > 0:
                    x, y = x + 1, y
                elif y - 1 >= 0 and fish_count[x][y - 1] > 0:
                    x, y = x, y - 1
                elif x - 1 >= 0 and fish_count[x - 1][y] > 0:
                    x, y = x - 1, y
            # If the current position does not have fish, move to the next position in any direction
            else:
                if y + 1 < c:
                    x, y = x, y + 1
                elif x + 1 < r:
                    x, y = x + 1, y
                elif y - 1 >= 0:
                    x, y = x, y - 1
                elif x - 1 >= 0:
                    x, y = x - 1, y
    
    # Return the maximum number of fish that can be caught
    return max(max_fish[x][y] for x in range(r) for y in range(c))

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    r, c, k, l, x0, y0 = map(int, input().split())
    times = []
    for _ in range(r):
        times.append(list(map(int, input().split())))
    print(f1(r, c, k, l, x0, y0, times))

