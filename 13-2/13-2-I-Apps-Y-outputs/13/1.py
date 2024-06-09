
def get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_to_reach = {intersection: float('inf') for intersection in intersections}
    time_to_reach[start_intersection] = 0
    
    # Initialize a queue to perform BFS
    queue = [start_intersection]
    
    while queue:
        current_intersection = queue.pop(0)
        current_time = time_to_reach[current_intersection]
        
        # Check if the current intersection is in Mister George's route
        if current_intersection in mister_george_route:
            # If it is, calculate the time it takes to reach the next intersection
            # by adding the time it takes to traverse the street between the current intersection and the next intersection
            next_intersection = mister_george_route[mister_george_route.index(current_intersection) + 1]
            time_to_reach[next_intersection] = current_time + streets[(current_intersection, next_intersection)]
            queue.append(next_intersection)
    
    # Return the least time it takes to reach the end intersection
    return time_to_reach[end_intersection]

def main():
    intersections, streets, start_intersection, end_intersection, mister_george_route, k = map(int, input().split())
    mister_george_route = list(map(int, input().split()))
    for _ in range(streets):
        a, b, l = map(int, input().split())
        streets[(a, b)] = l
    
    print(get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k))

if __name__ == '__main__':
    main()

