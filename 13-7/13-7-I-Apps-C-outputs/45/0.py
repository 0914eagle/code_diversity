
def get_shortest_time(N, y_coords, min_distances, r_time):
    # Initialize a dictionary to store the shortest time to reach each city
    shortest_time = {1: 0}
    for i in range(2, N+1):
        # Initialize the minimum time to reach city i as infinity
        min_time = float('inf')
        # Loop through all the cities j that are at a minimum distance from city i
        for j in range(1, N+1):
            if abs(y_coords[i-1] - y_coords[j-1]) >= min_distances[j-1]:
                # Calculate the total time to reach city j from city i
                total_time = r_time[j-1] + abs(y_coords[i-1] - y_coords[j-1])
                # If the total time is less than the minimum time, update the minimum time
                if total_time < min_time:
                    min_time = total_time
        # If there is a path to city i from city 1, add the minimum time to the shortest time dictionary
        if min_time < float('inf'):
            shortest_time[i] = min_time + shortest_time[i-1]
        # If there is no path to city i from city 1, set the shortest time to -1
        else:
            shortest_time[i] = -1
    return shortest_time

def main():
    N = int(input())
    y_coords = []
    min_distances = []
    r_time = []
    for i in range(N):
        y_coords.append(int(input()))
        min_distances.append(int(input()))
        r_time.append(int(input()))
    shortest_time = get_shortest_time(N, y_coords, min_distances, r_time)
    for i in range(1, N):
        print(shortest_time[i])

if __name__ == '__main__':
    main()

