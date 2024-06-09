
def f1(n, r, w, h):
    # Initialize the maximum number of gems to collect
    max_gems = 0
    # Initialize the current horizontal and vertical positions
    x, y = 0, 0
    # Initialize the list of gems
    gems = []
    # Read the input gems
    for i in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))
    # Sort the gems by their y-coordinate in descending order
    gems.sort(key=lambda x: x[1], reverse=True)
    # Iterate through the gems and collect them if they are within reach
    for gem in gems:
        # Calculate the distance to the gem
        distance = abs(gem[0] - x)
        # Check if the gem is within reach
        if distance <= r * (gem[1] - y):
            # Add the gem to the list of collected gems
            max_gems += 1
            # Update the current position
            x = gem[0]
            y = gem[1]
    # Return the maximum number of gems collected
    return max_gems

def f2(...):
    ...

if __name__ == '__main__':
    n, r, w, h = map(int, input().split())
    print(f1(n, r, w, h))

