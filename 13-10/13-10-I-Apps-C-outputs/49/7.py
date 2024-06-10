
def solve(n, traffic_lights):
    # Initialize the minimum time required to reach the end of the road
    min_time = 0
    
    # Loop through each traffic light
    for i in range(n-1):
        # Get the time, green duration, and red duration of the current traffic light
        t, g, r = traffic_lights[i]
        
        # If the current traffic light is green, add its duration to the minimum time
        if t <= 0:
            min_time += g
        
        # If the current traffic light is red, add its duration to the minimum time
        else:
            min_time += r
    
    # Return the minimum time required to reach the end of the road
    return min_time

def main():
    # Read the number of traffic lights
    n = int(input())
    
    # Initialize a list to store the times, green durations, and red durations of each traffic light
    traffic_lights = []
    
    # Loop through each traffic light
    for i in range(n-1):
        # Read the time, green duration, and red duration of the current traffic light
        t, g, r = map(int, input().split())
        
        # Add the current traffic light to the list
        traffic_lights.append((t, g, r))
    
    # Call the solve function with the number of traffic lights and the list of traffic lights
    print(solve(n, traffic_lights))

if __name__ == '__main__':
    main()

