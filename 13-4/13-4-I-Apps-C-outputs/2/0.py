
def f1(n, r, w, h):
    # Initialize variables
    gems = []
    max_gems = 0
    x_pos = 0
    y_pos = 0
    v_vel = 1
    h_vel = 0

    # Read input gems
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Sort gems by y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)

    # Iterate through gems and move towards them
    for gem in gems:
        # Calculate distance to gem
        dist = abs(gem[0] - x_pos)

        # Check if gem is reachable
        if dist <= v_vel * (h_vel / r):
            # Move towards gem
            h_vel = gem[0] - x_pos
            x_pos = gem[0]
            y_pos = gem[1]
            max_gems += 1

    return max_gems

def f2(...):
    ...

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))

