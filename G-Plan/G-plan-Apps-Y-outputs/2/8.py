
def count_good_observatories(N, M, elevations, roads):
    good_observatories = [True] * N
    
    for a, b in roads:
        if elevations[a-1] >= elevations[b-1]:
            good_observatories[b-1] = False
        if elevations[b-1] >= elevations[a-1]:
            good_observatories[a-1] = False
    
    return good_observatories.count(True)

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    
    result = count_good_observatories(N, M, elevations, roads)
    print(result)
