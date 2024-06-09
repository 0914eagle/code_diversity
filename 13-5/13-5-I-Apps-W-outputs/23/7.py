
def get_input():
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
    
    # Initialize a dictionary to keep track of the people assigned to each shelter
    assigned_people = {s_i-1: 0 for s_i, _ in shelters}
    
    # Initialize a priority queue to keep track of the locations with the most people to assign
    queue = [(people[i], i) for i in range(n)]
    heapq.heapify(queue)
    
    # While there are still people to assign
    while queue:
        # Get the location with the most people to assign
        people_to_assign, location = heapq.heappop(queue)
        
        # If the location has already been assigned to a shelter
        if location in assigned_people:
            # Decrement the number of people assigned to that shelter
            assigned_people[location] -= people_to_assign
        
        # Otherwise, assign the location to the shelter with the most capacity
        else:
            # Find the shelter with the most capacity
            max_capacity = max(shelters, key=lambda x: x[1])[1]
            
            # Assign the location to that shelter
            assigned_people[location] = people_to_assign
        
        # Update the number of people assigned to each shelter
        for s_i, c_i in shelters:
            assigned_people[s_i-1] += min(assigned_people[location], c_i)
        
        # Remove the location from the graph
        graph[location].clear()
    
    # Calculate the minimum time it takes to shelter everyone
    min_time = 0
    for u, v, w in roads:
        if assigned_people[u] > 0 and assigned_people[v] > 0:
            min_time += w
    
    return min_time

def main():
    n, m, s, people, roads, shelters = get_input()
    print(optimize_shelters(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

