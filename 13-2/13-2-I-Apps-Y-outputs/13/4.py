
def get_least_time(intersections, streets, start_intersection, end_intersection, k, mister_george_route):
    # Initialize a dictionary to store the time it takes to reach each intersection
    time_to_reach = {start_intersection: 0}
    for intersection in intersections:
        if intersection not in time_to_reach:
            time_to_reach[intersection] = float('inf')

    # Initialize a queue to store the intersections to visit
    queue = [start_intersection]

    # Loop until the queue is empty
    while queue:
        # Get the current intersection
        current_intersection = queue.pop(0)

        # If the current intersection is the end intersection, return the time it takes to reach it
        if current_intersection == end_intersection:
            return time_to_reach[current_intersection]

        # Get the list of streets that can be traversed from the current intersection
        streets_to_visit = [street for street in streets if street[0] == current_intersection or street[1] == current_intersection]

        # Loop through the list of streets to visit
        for street in streets_to_visit:
            # Get the time it takes to traverse the street
            time_to_traverse = street[2]

            # Get the intersection at the other end of the street
            other_intersection = street[0] if street[1] == current_intersection else street[1]

            # If the time it takes to reach the other intersection is greater than the time it takes to traverse the street, update the time it takes to reach the other intersection
            if time_to_reach[other_intersection] > time_to_reach[current_intersection] + time_to_traverse:
                time_to_reach[other_intersection] = time_to_reach[current_intersection] + time_to_traverse

                # Add the other intersection to the queue
                queue.append(other_intersection)

    # If the end intersection is not in the dictionary, it is not reachable
    if end_intersection not in time_to_reach:
        return -1

    # Return the time it takes to reach the end intersection
    return time_to_reach[end_intersection]

def main():
    # Read the input
    intersections, streets, start_intersection, end_intersection, k, mister_george_route = read_input()

    # Calculate the least time it takes to make the delivery
    least_time = get_least_time(intersections, streets, start_intersection, end_intersection, k, mister_george_route)

    # Print the result
    print(least_time)

def read_input():
    # Read the number of intersections and streets
    n, m = map(int, input().split())

    # Read the starting and ending intersections, and the difference in starting times between Mister George and Luka
    a, b, k, g = map(int, input().split())

    # Read the list of intersections Mister George will visit
    mister_george_route = list(map(int, input().split()))

    # Initialize a list to store the streets
    streets = []

    # Loop through the number of streets
    for _ in range(m):
        # Read the street information
        a, b, l = map(int, input().split())

        # Add the street to the list of streets
        streets.append((a, b, l))

    # Return the intersections, streets, starting intersection, ending intersection, difference in starting times, and the list of intersections Mister George will visit
    return range(1, n + 1), streets, a, b, k, mister_george_route

if __name__ == '__main__':
    main()

