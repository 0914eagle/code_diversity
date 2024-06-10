
def get_min_time(d, k, a, b, t):
    # Initialize variables
    time = 0
    distance = 0
    car_time = 0
    walk_time = 0
    
    # Loop until the post office is reached
    while distance < d:
        # Calculate the time it takes to drive the next segment
        if distance + k <= d:
            car_time = a * k
        else:
            car_time = a * (d - distance)
        
        # Calculate the time it takes to walk the next segment
        walk_time = b * (d - distance - k)
        
        # Add the time it takes to drive and walk to the total time
        time += car_time + walk_time
        
        # Increment the distance traveled
        distance += k
        
        # If the car breaks, add the time it takes to repair it
        if distance == k:
            time += t
    
    # Return the minimum time it takes to reach the post office
    return time

def main():
    d, k, a, b, t = map(int, input().split())
    print(get_min_time(d, k, a, b, t))

if __name__ == '__main__':
    main()

