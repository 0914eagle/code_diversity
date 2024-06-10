
def count_good_observatories(N, M, elevations, connections):
    good_observatories = 0
    reachable_observatories = [set() for _ in range(N)]
    
    for A, B in connections:
        reachable_observatories[A - 1].add(B - 1)
        reachable_observatories[B - 1].add(A - 1)
    
    for i in range(N):
        is_good = True
        for j in reachable_observatories[i]:
            if elevations[i] <= elevations[j]:
                is_good = False
                break
        if is_good:
            good_observatories += 1
    
    return good_observatories

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(M)]
    
    result = count_good_observatories(N, M, elevations, connections)
    print(result)
