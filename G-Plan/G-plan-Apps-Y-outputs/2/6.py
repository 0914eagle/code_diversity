
def count_good_observatories(N, M, elevations, roads):
    good_observatories = set(range(1, N + 1))
    
    for a, b in roads:
        if elevations[a - 1] >= elevations[b - 1]:
            good_observatories.discard(b)
        if elevations[b - 1] >= elevations[a - 1]:
            good_observatories.discard(a)
    
    return len(good_observatories)

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    
    result = count_good_observatories(N, M, elevations, roads)
    print(result)
