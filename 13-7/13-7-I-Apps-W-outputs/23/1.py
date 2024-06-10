
import math

def get_min_time(n, s, points):
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = math.inf
    
    # Iterate over all possible positions of the bomb
    for bomb_pos in range(10**6):
        # Initialize the time needed for both points 0 and 10^6 to be reached at the current bomb position
        time_needed = 0
        
        # Iterate over all people
        for person in points:
            # Calculate the distance between the person and the bomb
            dist = abs(person[0] - bomb_pos)
            
            # Calculate the time needed for the person to reach the bomb at their maximum speed
            time_needed += dist / person[1]
            
            # If the person is facing the bomb, their speed will increase by the ray's speed
            if person[2] == 1:
                time_needed += s / person[1]
        
        # If the time needed for both points 0 and 10^6 to be reached at the current bomb position is less than the minimum time, update the minimum time
        if time_needed < min_time:
            min_time = time_needed
    
    # Return the minimum time needed for both points 0 and 10^6 to be reached
    return min_time

def main():
    n, s = map(int, input().split())
    points = []
    for _ in range(n):
        x, v, t = map(int, input().split())
        points.append((x, v, t))
    print(get_min_time(n, s, points))

if __name__ == '__main__':
    main()

