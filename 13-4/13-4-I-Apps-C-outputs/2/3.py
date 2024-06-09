
def f1(n, r, w, h):
    # Initialize the variables
    gems = []
    max_gems = 0
    current_gems = 0
    x_position = 0
    y_position = 0
    vertical_velocity = 0
    horizontal_velocity = 0

    # Read the input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Loop through the gems and try to collect them
    for gem in gems:
        x, y = gem
        distance = abs(x - x_position)
        time = distance / horizontal_velocity
        if time <= vertical_velocity:
            current_gems += 1
            x_position = x
            y_position = y
        else:
            break

    # Update the maximum number of gems collected
    if current_gems > max_gems:
        max_gems = current_gems

    return max_gems

def f2(n, r, w, h):
    # Initialize the variables
    gems = []
    max_gems = 0
    current_gems = 0
    x_position = 0
    y_position = 0
    vertical_velocity = 0
    horizontal_velocity = 0

    # Read the input
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Loop through the gems and try to collect them
    for gem in gems:
        x, y = gem
        distance = abs(x - x_position)
        time = distance / horizontal_velocity
        if time <= vertical_velocity:
            current_gems += 1
            x_position = x
            y_position = y
        else:
            break

    # Update the maximum number of gems collected
    if current_gems > max_gems:
        max_gems = current_gems

    return max_gems

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))

