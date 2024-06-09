
def read_input():
    n, m, s = map(int, input().split())
    people = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    shelters = []
    for _ in range(s):
        s_i, c_i = map(int, input().split())
        shelters.append((s_i, c_i))
    return n, m, s, people, roads, shelters

def optimize_shelters(n, m, s, people, roads, shelters):
    # Initialize a graph with n locations and m roads
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    # Initialize a dictionary to keep track of the people at each location
    people_at_location = {i: people[i] for i in range(n)}
    
    # Initialize a dictionary to keep track of the people at each shelter
    people_at_shelter = {i: 0 for i, _ in shelters}
    
    # Initialize a dictionary to keep track of the time it takes to reach each shelter from each location
    time_to_reach_shelter = {i: float('inf') for i in range(n)}
    
    # Initialize a priority queue to keep track of the locations to visit
    queue = [(0, 0)]
    
    while queue:
        time, location = heapq.heappop(queue)
        if location in people_at_shelter:
            continue
        people_at_shelter[location] += people_at_location[location]
        for neighbor, weight in graph[location]:
            if time_to_reach_shelter[neighbor] > time + weight:
                time_to_reach_shelter[neighbor] = time + weight
                heapq.heappush(queue, (time + weight, neighbor))
    
    # Find the shelter with the minimum time to reach
    min_time = float('inf')
    min_shelter = None
    for shelter, time in time_to_reach_shelter.items():
        if time < min_time:
            min_time = time
            min_shelter = shelter
    
    # Return the minimum time to reach the shelter
    return min_time

def main():
    n, m, s, people, roads, shelters = read_input()
    print(optimize_shelters(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

