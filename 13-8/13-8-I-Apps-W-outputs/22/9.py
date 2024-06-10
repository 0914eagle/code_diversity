
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    direction = 1
    safety_island_reached = False
    
    # Iterate through the road segments
    for i in range(n):
        # Check if the current position is a safety island
        if current_position in d:
            safety_island_reached = True
        
        # Check if the current position is the end of the road
        if current_position == n:
            break
        
        # Update the current position and direction
        current_position += direction
        if safety_island_reached:
            direction = -direction
            safety_island_reached = False
        
        # Update the minimum time
        min_time += 1
    
    # Return the minimum time
    return min_time

def main():
    n, m = map(int, input().split())
    d = set(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

