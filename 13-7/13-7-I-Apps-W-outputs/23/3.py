
def get_min_time(n, s, people):
    # Initialize the minimum time needed for both points 0 and 10^6 to be reached
    min_time = float('inf')
    
    # Loop through all possible positions of the bomb
    for bomb_pos in range(10**6):
        # Initialize the time needed for both points 0 and 10^6 to be reached at the current bomb position
        time_needed = 0
        
        # Loop through all people
        for person in people:
            # Calculate the distance between the person and the bomb
            dist = abs(person[0] - bomb_pos)
            
            # Calculate the time needed for the person to reach the bomb at their maximum speed
            time_needed += dist / person[1]
            
            # Calculate the time needed for the person to reach the bomb at their maximum speed plus the speed of the rays
            time_needed += dist / (person[1] + s)
        
        # If the time needed for both points 0 and 10^6 to be reached at the current bomb position is less than the minimum time, update the minimum time
        if time_needed < min_time:
            min_time = time_needed
    
    # Return the minimum time needed for both points 0 and 10^6 to be reached
    return min_time

def main():
    # Read the number of people and the rays' speed
    n, s = map(int, input().split())
    
    # Read the description of the people
    people = []
    for _ in range(n):
        x, v, t = map(int, input().split())
        people.append((x, v, t))
    
    # Calculate the minimum time needed for both points 0 and 10^6 to be reached
    min_time = get_min_time(n, s, people)
    
    # Print the minimum time needed for both points 0 and 10^6 to be reached
    print(min_time)

if __name__ == '__main__':
    main()

