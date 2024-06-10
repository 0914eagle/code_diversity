
def get_remote_planets(planets, tunnels):
    # Initialize a dictionary to store the connections between planets
    connections = {}
    for tunnel in tunnels:
        connections[tunnel[0]] = connections.get(tunnel[0], set()) | {tunnel[1]}
        connections[tunnel[1]] = connections.get(tunnel[1], set()) | {tunnel[0]}

    # Find the planets that are not connected to the rest of the planets
    remote_planets = set()
    for planet in planets:
        if planet not in connections:
            remote_planets.add(planet)
        else:
            for connected_planet in connections[planet]:
                if connected_planet not in connections:
                    remote_planets.add(connected_planet)

    return len(remote_planets)

def main():
    num_planets = int(input())
    planets = set(range(1, num_planets + 1))
    tunnels = []
    for _ in range(num_planets - 1):
        tunnel = tuple(map(int, input().split()))
        tunnels.append(tunnel)

    print(get_remote_planets(planets, tunnels))

if __name__ == '__main__':
    main()

