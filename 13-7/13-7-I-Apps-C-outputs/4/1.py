
def get_gems(n, r, w, h, gems):
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
        # Calculate the vertical distance travelled during that time
        vertical_distance = vertical_velocity * time
        # Check if the gem is within reach
        if current_y - vertical_distance >= y:
            current_gems += 1
        # Update the current position and velocity
        current_x = x
        current_y = y
        horizontal_velocity = min(max(horizontal_velocity + (distance / (r * time)), -vertical_velocity / r), vertical_velocity / r)
        max_gems = max(max_gems, current_gems)

    return max_gems

def main():
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    print(get_gems(n, r, w, h, gems))

if __name__ == '__main__':
    main()

