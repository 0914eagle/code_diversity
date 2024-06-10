
import math

def get_velocity(n, mice, m):
    # Initialize the minimum velocity necessary to eat all mice
    min_velocity = 0
    
    # Loop through each mouse and calculate the minimum velocity necessary to eat it
    for mouse in mice:
        # Calculate the distance between the cat and the mouse
        distance = math.sqrt((mouse[0]) ** 2 + (mouse[1]) ** 2)
        
        # Calculate the time it takes for the cat to reach the mouse
        time = distance / min_velocity
        
        # If the cat reaches the mouse before it ducks underground, the minimum velocity necessary to eat it is the current minimum velocity
        if time < mouse[2]:
            min_velocity = min_velocity
        
        # If the cat doesn't reach the mouse before it ducks underground, the minimum velocity necessary to eat it is the current minimum velocity multiplied by the slowdown factor
        else:
            min_velocity = min_velocity * m
    
    # Return the minimum velocity necessary to eat all mice
    return min_velocity

def get_optimal_order(n, mice, m):
    # Initialize the optimal order of mice to eat
    optimal_order = []
    
    # Loop through each mouse and add it to the optimal order if it's the closest mouse to the cat
    for mouse in mice:
        # Calculate the distance between the cat and the mouse
        distance = math.sqrt((mouse[0]) ** 2 + (mouse[1]) ** 2)
        
        # If the mouse is the closest to the cat, add it to the optimal order
        if len(optimal_order) == 0 or distance < optimal_order[0][0]:
            optimal_order.append([distance, mouse])
        
        # If the mouse is not the closest to the cat, insert it into the optimal order in the correct position
        else:
            for i in range(len(optimal_order)):
                if distance < optimal_order[i][0]:
                    optimal_order.insert(i, [distance, mouse])
                    break
    
    # Return the optimal order of mice to eat
    return [mouse for distance, mouse in optimal_order]

def main():
    # Read the input
    n = int(input())
    mice = []
    for i in range(n):
        x, y, s = map(int, input().split())
        mice.append([x, y, s])
    m = float(input())
    
    # Calculate the minimum velocity necessary to eat all mice in the optimal order
    velocity = get_velocity(n, mice, m)
    
    # Print the minimum velocity necessary to eat all mice
    print(velocity)

if __name__ == '__main__':
    main()

