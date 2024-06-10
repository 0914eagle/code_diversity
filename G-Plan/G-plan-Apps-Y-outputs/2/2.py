
def count_good_observatories(N, M, elevations, connections):
    good_obs = 0
    reachable = [False] * N

    for a, b in connections:
        if elevations[a - 1] < elevations[b - 1]:
            reachable[a - 1] = True
        if elevations[b - 1] < elevations[a - 1]:
            reachable[b - 1] = True

    for i in range(N):
        if not any(reachable[j] for j in connections[i]):
            good_obs += 1

    return good_obs

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(M)]

    result = count_good_observatories(N, M, elevations, connections)
    print(result)
