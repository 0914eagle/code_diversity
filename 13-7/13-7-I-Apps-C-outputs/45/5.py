
def get_shortest_time(N, y_coords, min_dist, additional_time):
    # Initialize a dictionary to store the shortest time from city 1 to each city
    shortest_time = {1: 0}
    for i in range(2, N+1):
        # Initialize the minimum time to be the maximum possible value
        min_time = float('inf')
        # Iterate over all the cities that can be reached from city 1
        for j in range(1, N+1):
            # Check if the city is reachable from city 1
            if abs(y_coords[i-1] - y_coords[j-1]) >= min_dist[j-1]:
                # Calculate the total time to reach the city
                time = shortest_time[j] + abs(y_coords[i-1] - y_coords[j-1]) + additional_time[j-1]
                # Update the minimum time if the total time is less than the current minimum time
                min_time = min(min_time, time)
        # If there is no city that can be reached from city 1, return -1
        if min_time == float('inf'):
            return -1
        # Otherwise, update the shortest time dictionary
        shortest_time[i] = min_time
    # Return the shortest time from city 1 to city N
    return shortest_time[N]

def main():
    N = int(input())
    y_coords = []
    min_dist = []
    additional_time = []
    for i in range(N):
        y_coords.append(int(input()))
        min_dist.append(int(input()))
        additional_time.append(int(input()))
    print(get_shortest_time(N, y_coords, min_dist, additional_time))

if __name__ == '__main__':
    main()

