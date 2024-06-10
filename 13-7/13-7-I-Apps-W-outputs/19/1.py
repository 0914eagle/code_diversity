
def get_remote_planets(planets, tunnels):
    # Initialize a set to store the remote planets
    remote_planets = set()

    # Iterate over the tunnels
    for tunnel in tunnels:
        # If the tunnel is not a duplicate
        if tunnel not in remote_planets:
            # Add the tunnel to the set of remote planets
            remote_planets.add(tunnel)

    # Return the number of remote planets
    return len(remote_planets)

def main():
    # Read the number of planets and tunnels
    num_planets, num_tunnels = map(int, input().split())

    # Read the tunnels
    tunnels = []
    for _ in range(num_tunnels):
        tunnel = tuple(map(int, input().split()))
        tunnels.append(tunnel)

    # Get the number of remote planets
    num_remote_planets = get_remote_planets(num_planets, tunnels)

    # Print the number of remote planets
    print(num_remote_planets)

if __name__ == '__main__':
    main()

