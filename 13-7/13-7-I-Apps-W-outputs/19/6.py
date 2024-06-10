
def get_remote_planets(num_planets, tunnels):
    # Initialize a set to store the planets that are not remote
    non_remote_planets = set()

    # Iterate over the tunnels
    for tunnel in tunnels:
        # Add the planets in the tunnel to the set of non-remote planets
        non_remote_planets.add(tunnel[0])
        non_remote_planets.add(tunnel[1])

    # Return the number of planets that are not in the set of non-remote planets
    return num_planets - len(non_remote_planets)

def main():
    num_planets = int(input())
    tunnels = []

    for _ in range(num_planets - 1):
        tunnel = tuple(map(int, input().split()))
        tunnels.append(tunnel)

    print(get_remote_planets(num_planets, tunnels))

if __name__ == '__main__':
    main()

