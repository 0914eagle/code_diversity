
def get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_to_reach = {intersection: 0 for intersection in intersections}
    
    # Initialize a set to store the intersections that are blocked by Mister George
    blocked_intersections = set()
    
    # Iterate through the Mister George's route
    for i in range(len(mister_george_route) - 1):
        # Get the current and next intersection
        current_intersection = mister_george_route[i]
        next_intersection = mister_george_route[i + 1]
        
        # Get the time it takes to traverse the street between the current and next intersection
        street = (current_intersection, next_intersection)
        time_to_traverse = streets[street]
        
        # Update the time it takes to reach the next intersection
        time_to_reach[next_intersection] = time_to_reach[current_intersection] + time_to_traverse
        
        # Add the current intersection to the set of blocked intersections
        blocked_intersections.add(current_intersection)
    
    # Initialize the least time it takes to make the delivery
    least_time = float('inf')
    
    # Iterate through the possible starting times for Luka
    for start_time in range(k, k + 1000):
        # Get the time it takes to reach the start intersection
        time_to_start = time_to_reach[start_intersection] + start_time
        
        # Check if the start intersection is blocked by Mister George
        if time_to_start in blocked_intersections:
            continue
        
        # Get the time it takes to reach the end intersection
        time_to_end = time_to_reach[end_intersection] + time_to_start
        
        # Update the least time it takes to make the delivery
        least_time = min(least_time, time_to_end)
    
    return least_time

def main():
    # Read the input
    intersections, streets, start_intersection, end_intersection, mister_george_route, k = read_input()
    
    # Calculate the least time it takes to make the delivery
    least_time = get_least_time(intersections, streets, start_intersection, end_intersection, mister_george_route, k)
    
    # Print the result
    print(least_time)

def read_input():
    # Read the number of intersections and streets
    n, m = map(int, input().split())
    
    # Read the starting and ending intersections, and the difference in starting times between Mister George and Luka
    a, b, k, g = map(int, input().split())
    
    # Read the Mister George's route
    mister_george_route = list(map(int, input().split()))
    
    # Initialize a dictionary to store the streets and their times
    streets = {}
    
    # Read the streets and their times
    for _ in range(m):
        a, b, l = map(int, input().split())
        streets[(a, b)] = l
    
    return n, streets, a, b, mister_george_route, k

if __name__ == '__main__':
    main()

