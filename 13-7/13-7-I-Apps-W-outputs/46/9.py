
def get_earliest_arrival_time(flights_a_to_b, flights_b_to_c, max_cancellations, connection_time_a_to_b, connection_time_b_to_c):
    # Sort the flights from A to B and B to C by their departure times
    flights_a_to_b.sort()
    flights_b_to_c.sort()
    
    # Initialize the earliest arrival time as the last flight from B to C
    earliest_arrival_time = flights_b_to_c[-1]
    
    # Loop through the flights from A to B and B to C
    for i in range(len(flights_a_to_b)):
        for j in range(len(flights_b_to_c)):
            # Check if the flight from A to B and the flight from B to C can be connected
            if flights_b_to_c[j] >= flights_a_to_b[i] + connection_time_a_to_b:
                # Calculate the earliest arrival time by taking the current flight from A to B and the current flight from B to C
                earliest_arrival_time = min(earliest_arrival_time, flights_b_to_c[j] - connection_time_a_to_b)
    
    # If the earliest arrival time is still the last flight from B to C, it means that it is not possible to reach C at all
    if earliest_arrival_time == flights_b_to_c[-1]:
        return -1
    
    # Return the earliest arrival time
    return earliest_arrival_time

def main():
    # Read the input
    n, m, t_a, t_b, k = map(int, input().split())
    flights_a_to_b = list(map(int, input().split()))
    flights_b_to_c = list(map(int, input().split()))
    
    # Call the get_earliest_arrival_time function and print the result
    print(get_earliest_arrival_time(flights_a_to_b, flights_b_to_c, k, t_a, t_b))

if __name__ == '__main__':
    main()

