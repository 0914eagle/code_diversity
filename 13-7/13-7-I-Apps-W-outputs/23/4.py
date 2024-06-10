
def get_min_time(people, s):
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = float('inf')
    
    # Iterate over all possible bomb positions
    for bomb_pos in range(10**6):
        # Initialize the time needed for each person to reach the end point
        time_needed = [0] * len(people)
        
        # Iterate over all people
        for i, person in enumerate(people):
            # Calculate the distance between the person and the bomb
            dist = abs(bomb_pos - person[0])
            
            # If the person is facing the bomb, increase their speed
            if person[2] == 1:
                speed = person[1] + s
            else:
                speed = person[1]
            
            # Calculate the time needed for the person to reach the end point
            time_needed[i] = dist / speed
        
        # Calculate the maximum time needed for both points 0 and 10^6 to be reached
        max_time = max(time_needed)
        
        # If the maximum time is less than the current minimum time, update the minimum time
        if max_time < min_time:
            min_time = max_time
    
    # Return the minimum time needed for both points 0 and 10^6 to be reached
    return min_time

def main():
    # Read the input
    n, s = map(int, input().split())
    people = []
    for _ in range(n):
        x, v, t = map(int, input().split())
        people.append((x, v, t))
    
    # Find the minimum time needed for both points 0 and 10^6 to be reached
    min_time = get_min_time(people, s)
    
    # Print the minimum time
    print(min_time)

if __name__ == '__main__':
    main()

