
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
        # Calculate the distance to the gem
        distance = abs(current_x - x)
        # Calculate the time it will take to reach the gem
        time = distance / horizontal_velocity
        # Calculate the vertical distance travelled while reaching the gem
        vertical_distance = vertical_velocity * time
        # Calculate the horizontal distance travelled while reaching the gem
        horizontal_distance = horizontal_velocity * time
        # Check if the gem can be collected
        if vertical_distance <= y and horizontal_distance <= distance:
            current_gems += 1
        # Update the current position and velocity
        current_x = x
        current_y = y
        horizontal_velocity = min(max(horizontal_velocity + r, -vertical_velocity / r), vertical_velocity / r)
        vertical_velocity -= r
        max_gems = max(max_gems, current_gems)
    
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

