
def get_tunnel_cost(point1, point2):
    return min(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]), abs(point1[2] - point2[2]))

def get_min_cost(planets):
    cost = 0
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            cost += get_tunnel_cost(planets[i], planets[j])
    return cost

def main():
    num_planets = int(input())
    planets = []
    for i in range(num_planets):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    print(get_min_cost(planets))

if __name__ == '__main__':
    main()

