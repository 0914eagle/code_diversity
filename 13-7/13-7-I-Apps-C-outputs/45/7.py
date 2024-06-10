
def get_shortest_time(N, y_coords, min_dist, rest_time):
    # Initialize a dictionary to store the shortest time to reach each city
    shortest_time = {1: 0}
    for i in range(2, N+1):
        # Initialize the minimum time to reach city i as infinity
        min_time = float('inf')
        # Loop through all the cities that can be reached from city i-1
        for j in range(1, i):
            # Calculate the time to reach city j from city i-1
            time = shortest_time[j] + abs(y_coords[i-1] - y_coords[j-1]) + rest_time[j-1]
            # If the time to reach city j is less than the minimum time, update the minimum time
            if time < min_time:
                min_time = time
        # If there is a way to reach city i, add it to the dictionary with the minimum time
        if min_time != float('inf'):
            shortest_time[i] = min_time
        # Otherwise, set the minimum time to -1
        else:
            shortest_time[i] = -1
    return shortest_time

def main():
    N = int(input())
    y_coords = []
    min_dist = []
    rest_time = []
    for i in range(N):
        y_coords.append(int(input()))
        min_dist.append(int(input()))
        rest_time.append(int(input()))
    shortest_time = get_shortest_time(N, y_coords, min_dist, rest_time)
    for i in range(1, N):
        print(shortest_time[i])

if __name__ == '__main__':
    main()

