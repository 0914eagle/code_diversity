
def f1(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    velocity_x = 0
    velocity_y = v

    # Read input gems
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort gems by y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through gems and update current position and velocity
    for gem in gems:
        x, y = gem
        if current_y >= y:
            continue
        else:
            current_x = x
            current_y = y
            velocity_x = (x - current_x) / r
            velocity_y = v
            current_gems += 1
            max_gems = max(max_gems, current_gems)

    return max_gems

def f2(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0
    current_gems = 0
    current_x = 0
    current_y = 0
    velocity_x = 0
    velocity_y = v

    # Read input gems
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort gems by y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through gems and update current position and velocity
    for gem in gems:
        x, y = gem
        if current_y >= y:
            continue
        else:
            current_x = x
            current_y = y
            velocity_x = (x - current_x) / r
            velocity_y = v
            current_gems += 1
            max_gems = max(max_gems, current_gems)

    return max_gems

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))

