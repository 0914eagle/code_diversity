
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
    
    # Iterate through the Mister George's route and mark the intersections that are blocked
    for i in range(len(mister_george_route) - 1):
        intersection1 = mister_george_route[i]
        intersection2 = mister_george_route[i + 1]
        blocked_intersections.add(intersection1)
        blocked_intersections.add(intersection2)
    
    # Calculate the time it takes to reach the end intersection
    time_to_reach[end_intersection] = max(time_to_reach[start_intersection] + k, time_to_reach[end_intersection])
    
    # Iterate through the intersections and calculate the least time it takes to reach the end intersection
    least_time = float('inf')
    for intersection in intersections:
        if intersection not in blocked_intersections:
            least_time = min(least_time, time_to_reach[intersection])
    
    return least_time

def main():
    intersections, streets, start_intersection, end_intersection, mister_george_route, k = map(int, input().split())
    print(get_least_time(range(1, intersections + 1), streets, start_intersection, end_intersection, mister_george_route, k))

if __name__ == '__main__':
    main()

