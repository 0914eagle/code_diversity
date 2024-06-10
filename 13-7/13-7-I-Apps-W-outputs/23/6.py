
def solve(n, s, people):
    # Initialize the minimum time needed to reach both points as infinity
    min_time = float('inf')
    
    # Iterate over all possible positions of the bomb
    for bomb_pos in range(0, 10**6):
        # Initialize the time needed to reach point 0 and point 10**6 as infinity
        time_0 = float('inf')
        time_10_6 = float('inf')
        
        # Iterate over all people
        for person in people:
            # Calculate the distance between the person and the bomb
            dist = abs(person[0] - bomb_pos)
            
            # If the person is facing left and the bomb is to the left of the person
            if person[2] == 1 and bomb_pos < person[0]:
                # The person will run to the left with his maximum speed
                time_0 = min(time_0, dist / person[1])
            # If the person is facing right and the bomb is to the right of the person
            elif person[2] == 2 and bomb_pos > person[0]:
                # The person will run to the right with his maximum speed
                time_10_6 = min(time_10_6, dist / person[1])
        
        # If the time needed to reach both points is less than the minimum time needed so far
        if time_0 + time_10_6 < min_time:
            # Update the minimum time needed
            min_time = time_0 + time_10_6
    
    # Return the minimum time needed to reach both points
    return min_time

