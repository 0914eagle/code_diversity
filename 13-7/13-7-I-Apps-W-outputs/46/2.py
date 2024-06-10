
def get_earliest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights):
    # Sort the flights by departure time
    a_flights.sort()
    b_flights.sort()
    
    # Initialize the earliest arrival time as -1
    earliest_arrival_time = -1
    
    # Loop through each possible combination of flights to cancel
    for i in range(k + 1):
        # Get the number of flights to cancel from A to B
        num_cancel_a = i
        
        # Get the number of flights to cancel from B to C
        num_cancel_b = k - i
        
        # Check if it's possible to reach C with the current combination of flights to cancel
        if num_cancel_a <= n and num_cancel_b <= m:
            # Get the latest departure time from A to B
            latest_departure_a = a_flights[n - num_cancel_a] if num_cancel_a > 0 else 0
            
            # Get the earliest departure time from B to C
            earliest_departure_b = b_flights[num_cancel_b] if num_cancel_b > 0 else 0
            
            # Check if it's possible to reach C within the connection time
            if latest_departure_a + t_a <= earliest_departure_b:
                # Calculate the earliest arrival time
                arrival_time = latest_departure_a + t_a + earliest_departure_b
                
                # Update the earliest arrival time if necessary
                if earliest_arrival_time == -1 or arrival_time < earliest_arrival_time:
                    earliest_arrival_time = arrival_time
    
    return earliest_arrival_time

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    a_flights = list(map(int, input().split()))
    b_flights = list(map(int, input().split()))
    print(get_earliest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights))

if __name__ == '__main__':
    main()

