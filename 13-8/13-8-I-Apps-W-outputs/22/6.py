
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    direction = 1
    safety_island_position = 0
    green_light_time = g
    red_light_time = r
    safety_island_list = d
    
    # Loop until the end of the road is reached
    while current_position < n:
        # Check if the current position is a safety island
        if current_position in safety_island_list:
            safety_island_position = current_position
        
        # Check if the green light is on
        if green_light_time > 0:
            # Move in the current direction
            current_position += direction
            green_light_time -= 1
        else:
            # Change direction if necessary
            if current_position == safety_island_position:
                direction = -direction
            else:
                direction = 1
                safety_island_position = current_position
            
            # Wait for the red light
            red_light_time -= 1
            green_light_time = g
        
        # Increment the minimum time
        min_time += 1
    
    # Return the minimum time
    return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

