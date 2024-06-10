
def get_earliest_time(flights_a_to_b, flights_b_to_c, connection_time, cancellation_limit):
    # Sort the flights by departure time
    flights_a_to_b.sort()
    flights_b_to_c.sort()
    
    # Initialize the earliest time as the latest arrival time at B
    earliest_time = flights_a_to_b[-1] + connection_time + flights_b_to_c[-1]
    
    # Loop through the flights from A to B and find the earliest time that works
    for i in range(len(flights_a_to_b)):
        for j in range(len(flights_b_to_c)):
            # Check if the flight from B to C departures after the flight from A to B arrives
            if flights_b_to_c[j] >= flights_a_to_b[i] + connection_time:
                # Calculate the earliest time and break if it's earlier than the current earliest time
                earliest_time = min(earliest_time, flights_a_to_b[i] + connection_time + flights_b_to_c[j])
                if earliest_time < flights_a_to_b[-1] + connection_time + flights_b_to_c[-1]:
                    break
    
    # If the cancellation limit is exceeded, return -1
    if len(flights_a_to_b) - i > cancellation_limit or len(flights_b_to_c) - j > cancellation_limit:
        return -1
    
    return earliest_time

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    flights_a_to_b = list(map(int, input().split()))
    flights_b_to_c = list(map(int, input().split()))
    print(get_earliest_time(flights_a_to_b, flights_b_to_c, t_a, t_b, k))

if __name__ == '__main__':
    main()

