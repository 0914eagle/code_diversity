
def count_good_observatories(N, M, elevations, roads):
    reachable_from = [set() for _ in range(N)]
    for a, b in roads:
        reachable_from[a-1].add(b-1)
        reachable_from[b-1].add(a-1)
    
    good_observatories = 0
    for i in range(N):
        is_good = True
        for neighbor in reachable_from[i]:
            if elevations[i] <= elevations[neighbor]:
                is_good = False
                break
        if is_good:
            good_observatories += 1
    
    return good_observatories

# Input processing
N, M = map(int, input().split())
elevations = list(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = count_good_observatories(N, M, elevations, roads)
print(result)
