
def get_tunnel_cost(x1, y1, z1, x2, y2, z2):
    return min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

def get_min_cost(planets):
    cost = 0
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            cost += get_tunnel_cost(*planets[i], *planets[j])
    return cost

def main():
    n = int(input())
    planets = []
    for i in range(n):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    print(get_min_cost(planets))

if __name__ == '__main__':
    main()

