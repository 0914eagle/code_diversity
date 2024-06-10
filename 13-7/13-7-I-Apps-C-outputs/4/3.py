
def get_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    velocity = 0
    horizontal_velocity = 0
    vertical_velocity = 0
    
    # Sort the gems by their y-coordinate in descending order
    gems = sorted(gems, key=lambda x: x[1], reverse=True)
    
    # Iterate through the gems
    for gem in gems:
        # Calculate the distance between the current position and the next gem
        distance = abs(current_x - gem[0])
        
        # Calculate the time it will take to reach the next gem
        time = distance / velocity
        
        # Calculate the horizontal and vertical velocities at the time it will take to reach the next gem
        horizontal_velocity = velocity * (1 - r)
        vertical_velocity = velocity * r
        
        # Calculate the new position after reaching the next gem
        current_x = gem[0] + horizontal_velocity * time
        current_y = gem[1] - vertical_velocity * time
        
        # Check if the new position is within the bounds of the track
        if current_x >= 0 and current_x <= w and current_y >= 0 and current_y <= h:
            current_gems += 1
        else:
            break
    
    # Return the maximum number of gems collected
    return current_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    print(get_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

