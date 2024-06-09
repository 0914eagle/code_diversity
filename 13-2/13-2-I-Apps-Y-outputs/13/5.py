
def get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_to_reach = {intersection: 0 for intersection in intersections}
    
    # Initialize a set to store the intersections that are blocked by Mister George
    blocked_intersections = set()
    
    # Iterate through the streets and calculate the time it takes to reach each intersection
    for street in streets:
        intersection1, intersection2, time = street
        if intersection1 not in time_to_reach:
            time_to_reach[intersection1] = 0
        if intersection2 not in time_to_reach:
            time_to_reach[intersection2] = 0
        time_to_reach[intersection2] = max(time_to_reach[intersection1] + time, time_to_reach[intersection2])
    
    # Iterate through the Mister George's route and block the intersections
    for intersection in mister_george_route:
        blocked_intersections.add(intersection)
    
    # Initialize the least time to reach the end intersection
    least_time = 0
    
    # Iterate through the intersections and calculate the time it takes to reach the end intersection
    for intersection in intersections:
        if intersection == end_intersection:
            break
        if intersection in blocked_intersections:
            continue
        least_time += time_to_reach[intersection]
    
    # Return the least time to reach the end intersection
    return least_time + k

def main():
    intersections, streets, start_intersection, end_intersection, mister_george_route, k = map(int, input().split())
    mister_george_route = list(map(int, input().split()))
    streets = [list(map(int, input().split())) for _ in range(streets)]
    print(get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k))

if __name__ == '__main__':
    main()

