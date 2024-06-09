
def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    velocity_x = 0
    velocity_y = 0

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Loop through the gems and calculate the maximum number of gems that can be collected
    for gem in gems:
        x, y = gem
        distance = abs(current_x - x)
        time = distance / velocity_x
        if time <= 0:
            continue
        current_gems += 1
        max_gems = max(max_gems, current_gems)
        current_x = x
        current_y = y
        velocity_x = min(max(velocity_x + r, -velocity_x / r), velocity_x - velocity_x / r)
        velocity_y = min(max(velocity_y + r, -velocity_y / r), velocity_y - velocity_y / r)

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

