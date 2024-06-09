
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    vertical_velocity = 0
    horizontal_velocity = 0
    
    # Sort the gems by their y-coordinate in descending order
    gems = sorted(gems, key=lambda x: x[1], reverse=True)
    
    # Loop through the gems and calculate the maximum number of gems that can be collected
    for gem in gems:
        x, y = gem
        # Calculate the distance to the current gem
        distance = abs(current_x - x)
        # Calculate the time it takes to reach the current gem
        time = distance / horizontal_velocity
        # Calculate the vertical distance traveled while reaching the current gem
        vertical_distance = vertical_velocity * time
        # Calculate the new y-coordinate after reaching the current gem
        new_y = current_y - vertical_distance
        # Check if the new y-coordinate is greater than the current gem's y-coordinate
        if new_y > y:
            # Add the current gem to the list of collected gems
            current_gems.append(gem)
            # Update the current x-coordinate and y-coordinate
            current_x = x
            current_y = y
            # Update the maximum number of gems collected
            max_gems = max(max_gems, len(current_gems))
    
    return max_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    print(get_max_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

