
import sys

def get_remote_planets(planets, tunnels):
    # Initialize a set to store the connected planets
    connected_planets = set()

    # Add the first planet to the connected planets set
    connected_planets.add(planets[0])

    # Iterate through the tunnels
    for tunnel in tunnels:
        # If the current planet is not in the connected planets set, add it
        if tunnel[0] not in connected_planets:
            connected_planets.add(tunnel[0])
        # If the other planet in the tunnel is not in the connected planets set, add it
        if tunnel[1] not in connected_planets:
            connected_planets.add(tunnel[1])

    # Return the number of remote planets
    return len(planets) - len(connected_planets)

def main():
    # Read the number of planets and tunnels from stdin
    num_planets = int(input())
    num_tunnels = int(input())

    # Read the planets and tunnels from stdin
    planets = [int(input()) for _ in range(num_planets)]
    tunnels = [[int(x) for x in input().split()] for _ in range(num_tunnels)]

    # Call the get_remote_planets function and print the result
    print(get_remote_planets(planets, tunnels))

if __name__ == '__main__':
    main()

