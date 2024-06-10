
def get_remote_planets(n, tunnels):
    # Initialize a set to store the remote planets
    remote_planets = set()

    # Iterate over the tunnels
    for tunnel in tunnels:
        # If the tunnel is not in the set of remote planets, add it to the set
        if tunnel not in remote_planets:
            remote_planets.add(tunnel)

    # Return the number of remote planets
    return len(remote_planets)

def main():
    # Read the number of planets and tunnels
    n, m = map(int, input().split())

    # Read the tunnels
    tunnels = []
    for _ in range(m):
        u, v = map(int, input().split())
        tunnels.append((u, v))

    # Call the function to get the number of remote planets
    remote_planets = get_remote_planets(n, tunnels)

    # Print the number of remote planets
    print(remote_planets)

if __name__ == '__main__':
    main()

