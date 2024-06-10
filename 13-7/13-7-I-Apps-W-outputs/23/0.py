
def get_min_time(n, s, points):
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = float('inf')
    
    # Iterate over all possible positions of the bomb
    for bomb_position in range(1000000):
        # Initialize the time needed for both points 0 and 10^6 to be reached
        time_needed = 0
        
        # Iterate over all people
        for person in points:
            # Calculate the distance between the person and the bomb
            distance = abs(person[0] - bomb_position)
            
            # Calculate the time needed for the person to reach the bomb
            time_needed += distance / s
            
            # Calculate the time needed for the person to reach point 0 or 10^6
            time_needed += distance / person[1]
        
        # Check if the time needed for both points 0 and 10^6 to be reached is less than the current minimum
        if time_needed < min_time:
            min_time = time_needed
    
    # Return the minimum time needed for both points 0 and 10^6 to be reached
    return min_time

def main():
    # Read the input
    n, s = map(int, input().split())
    points = []
    for _ in range(n):
        points.append(list(map(int, input().split())))
    
    # Calculate the minimum time needed for both points 0 and 10^6 to be reached
    min_time = get_min_time(n, s, points)
    
    # Print the minimum time needed for both points 0 and 10^6 to be reached
    print(min_time)

if __name__ == '__main__':
    main()

