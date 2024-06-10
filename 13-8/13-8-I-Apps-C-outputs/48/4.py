
import math

def get_min_velocity(n, mice, m):
    # Initialize the minimum velocity as a large number
    min_velocity = 1000
    
    # Loop through all possible mouse combinations
    for combination in get_combinations(mice):
        # Calculate the total time it takes to eat all mice in the current combination
        total_time = get_total_time(combination, m)
        
        # If the total time is less than the minimum time, update the minimum velocity
        if total_time < min_velocity:
            min_velocity = total_time
    
    # Return the minimum velocity
    return min_velocity

def get_combinations(mice):
    # Initialize an empty list to store the combinations
    combinations = []
    
    # Loop through all possible combinations of mice
    for i in range(1, len(mice) + 1):
        # Get all combinations of length i
        combinations.extend(itertools.combinations(mice, i))
    
    # Return the list of combinations
    return combinations

def get_total_time(combination, m):
    # Initialize the total time as 0
    total_time = 0
    
    # Loop through all mice in the combination
    for i in range(len(combination)):
        # Calculate the time it takes to eat the current mouse
        time = get_eating_time(combination[i], m)
        
        # Add the time to the total time
        total_time += time
    
    # Return the total time
    return total_time

def get_eating_time(mouse, m):
    # Calculate the distance between the cat and the mouse
    distance = math.sqrt((mouse[0] ** 2) + (mouse[1] ** 2))
    
    # Calculate the time it takes to eat the mouse
    time = distance / mouse[2]
    
    # Return the time
    return time

if __name__ == '__main__':
    # Read the input
    n = int(input())
    mice = []
    for i in range(n):
        x, y, s = map(int, input().split())
        mice.append((x, y, s))
    m = float(input())
    
    # Call the function to get the minimum velocity
    min_velocity = get_min_velocity(n, mice, m)
    
    # Print the output
    print(min_velocity)

