
def get_planet_coordinates(n):
    
    coordinates = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        coordinates.append((x, y, z))
    return coordinates


def get_tunnel_cost(planet_coordinates):
    
    cost = 0
    for i in range(len(planet_coordinates)):
        for j in range(i + 1, len(planet_coordinates)):
            cost += min(abs(planet_coordinates[i][0] - planet_coordinates[j][0]),
                        abs(planet_coordinates[i][1] - planet_coordinates[j][1]),
                        abs(planet_coordinates[i][2] - planet_coordinates[j][2]))
    return cost


def solve(n):
    
    planet_coordinates = get_planet_coordinates(n)
    return get_tunnel_cost(planet_coordinates)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))

