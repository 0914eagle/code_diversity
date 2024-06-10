
def find_tunnel_cost(planets):
    cost = 0
    for i in range(len(planets)):
        for j in range(i+1, len(planets)):
            cost += min(abs(planets[i][0] - planets[j][0]), abs(planets[i][1] - planets[j][1]), abs(planets[i][2] - planets[j][2]))
    return cost

def main():
    num_planets = int(input())
    planets = []
    for i in range(num_planets):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    print(find_tunnel_cost(planets))

if __name__ == '__main__':
    main()

