
def solve(N, M, A, B, K, G, streets):
    # Initialize a dictionary to store the time it takes to travel between each pair of intersections
    travel_time = {}
    for street in streets:
        travel_time[street[0], street[1]] = street[2]
    
    # Initialize a list to store the intersections that Mister George will visit
    mister_george_intersections = [int(x) for x in input().split()]
    
    # Initialize a list to store the time it takes to travel between each pair of intersections for Mister George
    mister_george_travel_time = [0] * (N + 1)
    for i in range(G):
        current_intersection = mister_george_intersections[i]
        next_intersection = mister_george_intersections[i + 1]
        travel_time_current = travel_time[current_intersection, next_intersection]
        mister_george_travel_time[current_intersection] += travel_time_current
        mister_george_travel_time[next_intersection] += travel_time_current
    
    # Initialize a list to store the time it takes to travel between each pair of intersections for Luka
    luka_travel_time = [0] * (N + 1)
    for i in range(N + 1):
        if i != A:
            luka_travel_time[i] = mister_george_travel_time[i] + K
    
    # Find the shortest path between the starting intersection and the destination intersection
    import heapq
    queue = [(0, A, [])]
    visited = set()
    while queue:
        (cost, current_intersection, path) = heapq.heappop(queue)
        if current_intersection == B:
            return cost
        if current_intersection in visited:
            continue
        visited.add(current_intersection)
        for next_intersection in range(1, N + 1):
            if next_intersection not in visited and luka_travel_time[next_intersection] != 0:
                heapq.heappush(queue, (cost + luka_travel_time[next_intersection], next_intersection, path + [next_intersection]))
    return -1

