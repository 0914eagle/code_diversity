
def get_earliest_arrival_time(flights_a_to_b, flights_b_to_c, k):
    # Sort the flights by departure time
    flights_a_to_b.sort()
    flights_b_to_c.sort()
    
    # Initialize the earliest arrival time as the last flight from B to C
    earliest_arrival_time = flights_b_to_c[-1]
    
    # Iterate through the flights from A to B
    for i in range(len(flights_a_to_b)):
        # Get the departure time of the current flight from A to B
        departure_time = flights_a_to_b[i]
        
        # Find the earliest arrival time from B to C that is greater than or equal to the departure time from A to B
        earliest_arrival_time_from_b_to_c = next((x for x in flights_b_to_c if x >= departure_time), None)
        
        # If there is no such arrival time, break the loop
        if earliest_arrival_time_from_b_to_c is None:
            break
        
        # Update the earliest arrival time if necessary
        earliest_arrival_time = max(earliest_arrival_time, earliest_arrival_time_from_b_to_c)
    
    # If we can cancel at most k flights, return the earliest arrival time
    if k >= len(flights_a_to_b) + len(flights_b_to_c):
        return earliest_arrival_time
    
    # Otherwise, return -1
    return -1

def get_latest_arrival_time(flights_a_to_b, flights_b_to_c, k):
    # Sort the flights by departure time
    flights_a_to_b.sort()
    flights_b_to_c.sort()
    
    # Initialize the latest arrival time as the last flight from B to C
    latest_arrival_time = flights_b_to_c[-1]
    
    # Iterate through the flights from A to B
    for i in range(len(flights_a_to_b)):
        # Get the departure time of the current flight from A to B
        departure_time = flights_a_to_b[i]
        
        # Find the latest arrival time from B to C that is greater than or equal to the departure time from A to B
        latest_arrival_time_from_b_to_c = next((x for x in flights_b_to_c if x >= departure_time), None)
        
        # If there is no such arrival time, break the loop
        if latest_arrival_time_from_b_to_c is None:
            break
        
        # Update the latest arrival time if necessary
        latest_arrival_time = min(latest_arrival_time, latest_arrival_time_from_b_to_c)
    
    # If we can cancel at most k flights, return the latest arrival time
    if k >= len(flights_a_to_b) + len(flights_b_to_c):
        return latest_arrival_time
    
    # Otherwise, return -1
    return -1

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    flights_a_to_b = list(map(int, input().split()))
    flights_b_to_c = list(map(int, input().split()))
    
    earliest_arrival_time = get_earliest_arrival_time(flights_a_to_b, flights_b_to_c, k)
    latest_arrival_time = get_latest_arrival_time(flights_a_to_b, flights_b_to_c, k)
    
    print(earliest_arrival_time)
    print(latest_arrival_time)

if __name__ == '__main__':
    main()

