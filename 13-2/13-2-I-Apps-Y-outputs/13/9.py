
def get_least_time(intersections, streets, luka_start, luka_end, mister_george_route, mister_george_start, mister_george_time):
    # Initialize a dictionary to store the time it takes to travel between each intersection
    time_dict = {}
    for street in streets:
        time_dict[street[0]] = street[2]
    
    # Initialize a list to store the intersections on Mister George's route
    mister_george_route_list = []
    for i in range(mister_george_start, mister_george_start + mister_george_time):
        mister_george_route_list.append(mister_george_route[i % len(mister_george_route)])
    
    # Initialize a set to store the intersections that are blocked by Mister George
    blocked_intersections = set()
    for i in range(len(mister_george_route_list) - 1):
        blocked_intersections.add(mister_george_route_list[i])
        blocked_intersections.add(mister_george_route_list[i + 1])
    
    # Initialize a queue to store the intersections that need to be visited
    queue = []
    queue.append(luka_start)
    
    # Initialize a dictionary to store the shortest time it takes to get to each intersection from the starting intersection
    shortest_time = {}
    shortest_time[luka_start] = 0
    
    # Initialize a dictionary to store the previous intersection for each intersection
    previous_intersection = {}
    previous_intersection[luka_start] = None
    
    # Loop until the queue is empty
    while queue:
        # Get the current intersection from the queue
        current_intersection = queue.pop(0)
        
        # If the current intersection is not blocked by Mister George, add it to the set of intersections that need to be visited
        if current_intersection not in blocked_intersections:
            queue.append(current_intersection)
        
        # If the current intersection is the end intersection, return the shortest time it takes to get there
        if current_intersection == luka_end:
            return shortest_time[current_intersection]
        
        # Loop through the neighbors of the current intersection
        for neighbor in intersections[current_intersection]:
            # If the neighbor is not blocked by Mister George and has not been visited yet, add it to the queue and update the shortest time and previous intersection
            if neighbor not in blocked_intersections and neighbor not in shortest_time:
                queue.append(neighbor)
                shortest_time[neighbor] = shortest_time[current_intersection] + time_dict[current_intersection][neighbor]
                previous_intersection[neighbor] = current_intersection
    
    # If the end intersection is not reached, return -1
    return -1

def main():
    intersections = {}
    streets = []
    luka_start, luka_end, k, g = map(int, input().split())
    mister_george_route = list(map(int, input().split()))
    for i in range(g):
        a, b, l = map(int, input().split())
        streets.append((a, b, l))
        if a not in intersections:
            intersections[a] = []
        if b not in intersections:
            intersections[b] = []
        intersections[a].append(b)
        intersections[b].append(a)
    print(get_least_time(intersections, streets, luka_start, luka_end, mister_george_route, k, g))

if __name__ == '__main__':
    main()

