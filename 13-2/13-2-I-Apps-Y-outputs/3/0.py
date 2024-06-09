
def f1(n, times, distances):
    # Initialize a list to store the speeds
    speeds = []
    
    # Iterate over the times and distances
    for i in range(n):
        # Calculate the speed using the distance and time differences
        speed = (distances[i] - distances[i-1]) / (times[i] - times[i-1])
        speeds.append(speed)
    
    # Return the maximum speed
    return max(speeds)

def f2(n, times, distances):
    # Initialize a list to store the speeds
    speeds = []
    
    # Iterate over the times and distances
    for i in range(n):
        # Calculate the speed using the distance and time differences
        speed = (distances[i] - distances[i-1]) / (times[i] - times[i-1])
        speeds.append(speed)
    
    # Return the maximum speed
    return max(speeds)

if __name__ == '__main__':
    n = int(input())
    times = []
    distances = []
    for i in range(n):
        t, d = map(int, input().split())
        times.append(t)
        distances.append(d)
    print(f1(n, times, distances))
    print(f2(n, times, distances))

