
import math

def get_min_velocity(mice, m):
    # Sort the mice by their ducking time in ascending order
    mice.sort(key=lambda x: x[2])
    
    # Initialize the minimum velocity and the current velocity
    min_velocity = 0
    velocity = 1
    
    # Loop through the mice and calculate the minimum velocity needed to catch each one
    for mouse in mice:
        # Calculate the time it takes for the cat to reach the mouse
        time_to_mouse = math.sqrt((mouse[0] ** 2) + (mouse[1] ** 2))
        
        # Calculate the time it takes for the cat to eat the mouse
        time_to_eat = time_to_mouse / velocity
        
        # Calculate the time it takes for the mouse to duck underground
        time_to_duck = mouse[2]
        
        # Calculate the minimum velocity needed to catch the mouse
        min_velocity_needed = velocity * (1 - (time_to_eat / time_to_duck))
        
        # Update the minimum velocity
        min_velocity = max(min_velocity, min_velocity_needed)
        
        # Update the current velocity
        velocity *= m
    
    return min_velocity

def main():
    # Read the number of mice and the multiplicative factor
    n, m = map(int, input().split())
    
    # Read the mice's coordinates and ducking time
    mice = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        mice.append((x, y, s))
    
    # Calculate the minimum velocity needed to catch all the mice
    min_velocity = get_min_velocity(mice, m)
    
    # Print the minimum velocity
    print(min_velocity)

if __name__ == '__main__':
    main()

