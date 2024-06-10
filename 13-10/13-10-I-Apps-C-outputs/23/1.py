
def read_input():
    N = int(input())
    planets = []
    for i in range(N):
        x, y, z = map(int, input().split())
        planets.append((x, y, z))
    return N, planets

def tunnel_cost(A, B):
    return min(abs(A[0] - B[0]), abs(A[1] - B[1]), abs(A[2] - B[2]))

def solve(N, planets):
    cost = 0
    for i in range(N):
        for j in range(i+1, N):
            cost += tunnel_cost(planets[i], planets[j])
    return cost

def main():
    N, planets = read_input()
    print(solve(N, planets))

if __name__ == '__main__':
    main()

