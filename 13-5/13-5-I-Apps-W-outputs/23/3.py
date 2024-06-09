
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
    
    # Initialize a dictionary to keep track of the shelters and their capacities
    shelter_capacities = {s_i: c_i for s_i, c_i in shelters}
    
    # Initialize a dictionary to keep track of the minimum time it takes to reach each shelter
    min_time_to_reach_shelter = {s_i: float('inf') for s_i in range(s)}
    
    # Initialize a dictionary to keep track of the people at each shelter
    people_at_shelter = {s_i: 0 for s_i in range(s)}
    
    # Initialize a queue to keep track of the locations to visit
    queue = []
    
    # Enqueue the first location
    queue.append(0)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a location
        location = queue.pop(0)
        
        # If the location has people, assign them to the nearest shelter
        if people_at_location[location]:
            # Find the nearest shelter
            nearest_shelter = min(shelter_capacities, key=lambda s_i: abs(location - s_i))
            
            # Assign the people to the nearest shelter
            people_at_shelter[nearest_shelter] += people_at_location[location]
            people_at_location[location] = 0
            
            # Update the minimum time to reach the nearest shelter
            min_time_to_reach_shelter[nearest_shelter] = min(min_time_to_reach_shelter[nearest_shelter], location)
        
        # Enqueue the neighbors of the current location
        for neighbor, weight in graph[location]:
            queue.append(neighbor)
    
    # Calculate the total time it takes to reach all shelters
    total_time = 0
    for s_i in range(s):
        total_time += min_time_to_reach_shelter[s_i] + people_at_shelter[s_i] * shelter_capacities[s_i]
    
    return total_time

def main():
    n, m, s, people, roads, shelters = read_input()
    print(optimize_shelters(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

