
def get_min_time(n, s, points):
    # Sort the points by their x coordinate
    points.sort(key=lambda x: x[0])
    
    # Initialize the minimum time needed to reach 0 and 10^6
    min_time_0 = 0
    min_time_10_6 = 0
    
    # Initialize the current position and speed of each person
    current_position = [point[0] for point in points]
    current_speed = [point[1] for point in points]
    
    # Iterate through each point
    for i in range(n):
        # Get the current point and its direction
        point = points[i]
        direction = point[2]
        
        # Update the current position and speed of the person
        current_position[i] += current_speed[i]
        current_speed[i] += s * direction
        
        # Check if the person has reached 0 or 10^6
        if current_position[i] == 0:
            min_time_0 = i + 1
        elif current_position[i] == 10**6:
            min_time_10_6 = i + 1
    
    # Return the minimum time needed to reach 0 and 10^6
    return min(min_time_0, min_time_10_6)

def main():
    n, s = map(int, input().split())
    points = []
    for i in range(n):
        x, v, t = map(int, input().split())
        points.append([x, v, t])
    print(get_min_time(n, s, points))

if __name__ == '__main__':
    main()

