
def get_min_time(n, s, points):
    # Sort the points by their x-coordinate
    points.sort(key=lambda x: x[0])
    
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = 10**18
    
    # Loop through each point and calculate the time needed for it to be reached
    for i in range(n):
        # Calculate the time needed for the current point to be reached
        time = (points[i][0] - points[0][0]) / points[i][1]
        
        # If the current point is the last point, add the time needed for the rays to catch up
        if i == n - 1:
            time += (10**6 - points[i][0]) / s
        
        # Update the minimum time needed if the current point is reached before the previous point
        if time < min_time:
            min_time = time
    
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

