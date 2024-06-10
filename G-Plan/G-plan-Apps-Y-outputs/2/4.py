
def count_good_observatories(N, M, elevations, roads):
    good_observatories = 0
    reachable_observatories = [set() for _ in range(N)]
    
    for a, b in roads:
        reachable_observatories[a - 1].add(b)
        reachable_observatories[b - 1].add(a)
    
    for i in range(N):
        is_good = True
        for j in reachable_observatories[i]:
            if elevations[i] <= elevations[j - 1]:
                is_good = False
                break
        if is_good:
            good_observatories += 1
    
    return good_observatories

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    
    result = count_good_observatories(N, M, elevations, roads)
    print(result)
