
def count_good_observatories(N, M, elevations, connections):
    good_observatories = set(range(1, N + 1))

    for A, B in connections:
        if elevations[A - 1] >= elevations[B - 1]:
            good_observatories.discard(B)
        if elevations[B - 1] >= elevations[A - 1]:
            good_observatories.discard(A)

    return len(good_observatories)

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(M)]

    result = count_good_observatories(N, M, elevations, connections)
    print(result)
