
import math

def get_tide_level(t):
    
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_square_height(x, y):
    
    return heights[y][x]

def is_safe_to_enter_square(x, y):
    
    # Get the height of the square
    square_height = get_square_height(x, y)
    
    # Get the tide level
    tide_level = get_tide_level(t)
    
    # Check if the square is dry
    if square_height <= tide_level:
        return True
    else:
        return False

def find_farthest_reachable_point(start_x, start_y):
    
    # Initialize the farthest reachable point as the starting point
    farthest_x = start_x
    farthest_y = start_y
    
    # Loop through all the squares
    for x in range(W):
        for y in range(H):
            # Check if it is safe to enter the square
            if is_safe_to_enter_square(x, y):
                # Calculate the distance between the current square and the starting point
                distance = math.sqrt((x - start_x) ** 2 + (y - start_y) ** 2)
                
                # Update the farthest reachable point if the current square is farther away than the current farthest reachable point
                if distance > math.sqrt((farthest_x - start_x) ** 2 + (farthest_y - start_y) ** 2):
                    farthest_x = x
                    farthest_y = y
    
    # Return the farthest reachable point
    return (farthest_x, farthest_y)

def main():
    # Read the input
    global a, m, W, H, heights, t
    a, m = map(float, input().split())
    W, H, X, Y = map(int, input().split())
    heights = []
    for _ in range(H):
        heights.append(list(map(int, input().split())))
    t = 0
    
    # Find the farthest reachable point
    farthest_x, farthest_y = find_farthest_reachable_point(X, Y)
    
    # Calculate the distance between the starting point and the farthest reachable point
    distance = math.sqrt((farthest_x - X) ** 2 + (farthest_y - Y) ** 2)
    
    # Print the result
    print(distance)

if __name__ == '__main__':
    main()

