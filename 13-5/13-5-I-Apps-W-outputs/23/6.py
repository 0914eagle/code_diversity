
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

def solve(n, m, s, people, roads, shelters):
    # create a graph with n locations and m roads
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    # create a dictionary to map each location to its shelter and capacity
    shelter_map = {}
    for s_i, c_i in shelters:
        shelter_map[s_i-1] = (c_i, 0)
    
    # create a queue to store the locations that need to be processed
    queue = []
    
    # initialize the first location to process
    queue.append(0)
    
    # loop until the queue is empty
    while queue:
        # get the current location from the queue
        curr_loc = queue.pop(0)
        
        # if the current location has not been assigned a shelter yet, assign it to the closest shelter
        if shelter_map[curr_loc][1] == 0:
            # find the closest shelter
            min_dist = float('inf')
            min_shelter = -1
            for s_i, c_i in shelter_map.items():
                dist = abs(curr_loc - s_i)
                if dist < min_dist:
                    min_dist = dist
                    min_shelter = s_i
            
            # assign the current location to the closest shelter
            shelter_map[curr_loc] = (shelter_map[min_shelter][0], min_shelter)
        
        # add the current location's neighbors to the queue
        for neighbor, weight in graph[curr_loc]:
            queue.append(neighbor)
    
    # calculate the minimum time it takes to shelter everyone
    time = 0
    for loc, (capacity, shelter) in shelter_map.items():
        if capacity < people[loc]:
            return -1
        time += people[loc] * (abs(loc - shelter) + 1)
    
    return time

def main():
    n, m, s, people, roads, shelters = get_input()
    print(solve(n, m, s, people, roads, shelters))

if __name__ == '__main__':
    main()

