
import sys
import math

def get_danger_level(chambers, tunnels):
    # Initialize the danger level of each chamber to 0
    danger_level = [0] * len(chambers)

    # Iterate over the tunnels
    for tunnel in tunnels:
        # Get the indices of the chambers connected by the tunnel
        chamber1, chamber2 = tunnel[0] - 1, tunnel[1] - 1

        # Update the danger level of the two chambers
        danger_level[chamber1] += tunnel[2]
        danger_level[chamber2] += tunnel[2]

    # Return the danger level of each chamber
    return danger_level

def main():
    # Read the number of chambers and tunnels
    num_chambers, num_tunnels = map(int, input().split())

    # Read the tunnels
    tunnels = []
    for _ in range(num_tunnels):
        tunnel = list(map(int, input().split()))
        tunnels.append(tunnel)

    # Get the danger level of each chamber
    danger_level = get_danger_level(range(1, num_chambers + 1), tunnels)

    # Print the danger level of each chamber
    print(*[d % 1000000007 for d in danger_level])

if __name__ == '__main__':
    main()

