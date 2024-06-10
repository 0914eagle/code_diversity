
def get_min_time(n, s, points):
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = float('inf')
    
    # Iterate over all possible positions of the bomb
    for bomb_pos in range(10**6):
        # Initialize the time needed for both points to be reached
        time_0 = float('inf')
        time_10_6 = float('inf')
        
        # Iterate over all people
        for i in range(n):
            # Get the person's position, speed, and direction
            x, v, t = points[i]
            
            # Calculate the time needed for the person to reach point 0
            time_0_i = (bomb_pos - x) / v
            
            # Calculate the time needed for the person to reach point 10^6
            time_10_6_i = (x - bomb_pos) / v
            
            # Update the minimum time needed for point 0
            time_0 = min(time_0, time_0_i)
            
            # Update the minimum time needed for point 10^6
            time_10_6 = min(time_10_6, time_10_6_i)
        
        # Calculate the minimum time needed for both points to be reached
        min_time = min(min_time, time_0 + time_10_6)
    
    return min_time

def main():
    n, s = map(int, input().split())
    points = []
    for i in range(n):
        x, v, t = map(int, input().split())
        points.append((x, v, t))
    print(get_min_time(n, s, points))

if __name__ == '__main__':
    main()

