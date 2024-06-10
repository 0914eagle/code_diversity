
def get_remote_planets(planets, tunnels):
    # Initialize a set to store the remote planets
    remote_planets = set()

    # Loop through each planet and its neighbors
    for planet, neighbors in tunnels.items():
        # If the planet has only one neighbor, it is a remote planet
        if len(neighbors) == 1:
            remote_planets.add(planet)

    # Return the number of remote planets
    return len(remote_planets)

def main():
    # Read the number of planets and tunnels from stdin
    num_planets = int(input())
    tunnels = {}
    for _ in range(num_planets - 1):
        u, v = map(int, input().split())
        if u not in tunnels:
            tunnels[u] = set()
        if v not in tunnels:
            tunnels[v] = set()
        tunnels[u].add(v)
        tunnels[v].add(u)

    # Call the function to get the number of remote planets
    num_remote_planets = get_remote_planets(num_planets, tunnels)

    # Print the number of remote planets
    print(num_remote_planets)

if __name__ == '__main__':
    main()

