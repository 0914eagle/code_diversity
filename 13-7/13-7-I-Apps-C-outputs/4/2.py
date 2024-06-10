
import sys

def get_max_gems(n, r, w, h, gems):
    # Initialize variables
    max_gems = 0
    current_gems = 0
    current_position = (0, 0)
    velocity = (0, v)

    # Sort the gems by their y-coordinate in descending order
    sorted_gems = sorted(gems, key=lambda x: x[1], reverse=True)

    # Iterate through the gems and calculate the maximum number of gems that can be collected
    for gem in sorted_gems:
        # Calculate the distance to the current gem
        distance = (gem[0] - current_position[0]) ** 2 + (gem[1] - current_position[1]) ** 2

        # If the distance is less than or equal to the maximum horizontal speed, collect the gem
        if distance <= (v / r) ** 2:
            current_gems += 1
            current_position = gem

        # If the current position is above the finish line, break the loop
        if current_position[1] >= h:
            break

    # Return the maximum number of gems collected
    return current_gems

def main():
    # Read the input
    n, r, w, h = map(int, input().split())
    gems = []
    for _ in range(n):
        x, y = map(int, input().split())
        gems.append((x, y))

    # Calculate the maximum number of gems that can be collected
    max_gems = get_max_gems(n, r, w, h, gems)

    # Print the result
    print(max_gems)

if __name__ == '__main__':
    main()

