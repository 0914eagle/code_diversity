
def count_good_observatories(N, M, elevations, connections):
    good_obs = [True] * N
    for a, b in connections:
        if elevations[a-1] >= elevations[b-1]:
            good_obs[b-1] = False
        if elevations[b-1] >= elevations[a-1]:
            good_obs[a-1] = False
    return sum(good_obs)

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(M)]
    result = count_good_observatories(N, M, elevations, connections)
    print(result)
