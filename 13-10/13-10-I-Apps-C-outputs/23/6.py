
import itertools

def read_input():
    N = int(input())
    planets = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    return N, planets

def tunnel_cost(planets, i, j):
    return min(abs(planets[i][0] - planets[j][0]), abs(planets[i][1] - planets[j][1]), abs(planets[i][2] - planets[j][2]))

def form_network(N, planets):
    costs = []
    for i in range(N):
        for j in range(i+1, N):
            costs.append(tunnel_cost(planets, i, j))
    return sum(costs)

def main():
    N, planets = read_input()
    print(form_network(N, planets))

if __name__ == '__main__':
    main()

