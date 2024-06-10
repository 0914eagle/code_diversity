
def get_remote_planets(planets, tunnels):
    # Initialize a set to store the connected planets
    connected_planets = set()

    # Loop through the tunnels and add the connected planets to the set
    for tunnel in tunnels:
        connected_planets.add(tunnel[0])
        connected_planets.add(tunnel[1])

    # Return the number of planets that are not in the connected set
    return len(planets) - len(connected_planets)

def main():
    # Read the number of planets and tunnels from stdin
    num_planets = int(input())
    num_tunnels = int(input())

    # Read the tunnels from stdin
    tunnels = []
    for _ in range(num_tunnels):
        tunnel = [int(x) for x in input().split()]
        tunnels.append(tunnel)

    # Get the set of remote planets
    remote_planets = get_remote_planets(set(range(1, num_planets + 1)), tunnels)

    # Print the number of remote planets
    print(remote_planets)

if __name__ == '__main__':
    main()

