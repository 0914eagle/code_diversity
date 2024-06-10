
def get_min_time(n, m, d, g, r):
    # Initialize variables
    min_time = 0
    current_position = 0
    direction = 1
    safety_islands = set(d)
    safety_island_count = len(safety_islands)
    
    # Loop until the end of the road is reached
    while current_position < n:
        # Check if the current position is a safety island
        if current_position in safety_islands:
            # If it is a safety island, change direction
            direction = -direction
            safety_island_count -= 1
            if safety_island_count == 0:
                # If there are no more safety islands, wait for the red light
                min_time += r
        else:
            # If it is not a safety island, move in the current direction
            current_position += direction
        
        # Increase the time by the green light time
        min_time += g
    
    return min_time

def main():
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    g, r = map(int, input().split())
    print(get_min_time(n, m, d, g, r))

if __name__ == '__main__':
    main()

