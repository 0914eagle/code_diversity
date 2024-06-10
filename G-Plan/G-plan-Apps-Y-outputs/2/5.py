
def count_good_observatories(N, M, elevations, connections):
    reachable = [False] * N
    good_observatories = 0
    
    for i in range(M):
        a, b = connections[i]
        if elevations[a-1] > elevations[b-1]:
            reachable[b-1] = True
        if elevations[b-1] > elevations[a-1]:
            reachable[a-1] = True
    
    for i in range(N):
        if not any(reachable[j] for j in range(N) if (i+1) in connections[j]):
            good_observatories += 1
    
    return good_observatories

if __name__ == "__main__":
    N, M = map(int, input().split())
    elevations = list(map(int, input().split()))
    connections = [list(map(int, input().split())) for _ in range(M)]
    
    result = count_good_observatories(N, M, elevations, connections)
    print(result)
