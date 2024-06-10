
def get_earliest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights):
    # Sort the flights by departure time
    a_flights.sort()
    b_flights.sort()
    
    # Initialize the earliest arrival time as the last flight from B to C
    earliest_arrival_time = b_flights[-1]
    
    # Iterate through the flights from A to B
    for i in range(n):
        # Find the corresponding flight from B to C that departs after the current flight from A to B arrives
        j = 0
        while j < m and b_flights[j] < a_flights[i] + t_a:
            j += 1
        
        # If there is a corresponding flight from B to C, update the earliest arrival time
        if j < m:
            earliest_arrival_time = min(earliest_arrival_time, b_flights[j])
    
    return earliest_arrival_time

def get_latest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights):
    # Sort the flights by departure time
    a_flights.sort()
    b_flights.sort()
    
    # Initialize the latest arrival time as the last flight from B to C
    latest_arrival_time = b_flights[-1]
    
    # Iterate through the flights from A to B
    for i in range(n):
        # Find the corresponding flight from B to C that departs after the current flight from A to B arrives
        j = 0
        while j < m and b_flights[j] < a_flights[i] + t_a:
            j += 1
        
        # If there is a corresponding flight from B to C, update the latest arrival time
        if j < m:
            latest_arrival_time = max(latest_arrival_time, b_flights[j])
    
    return latest_arrival_time

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    a_flights = list(map(int, input().split()))
    b_flights = list(map(int, input().split()))
    
    earliest_arrival_time = get_earliest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights)
    latest_arrival_time = get_latest_arrival_time(n, m, t_a, t_b, k, a_flights, b_flights)
    
    if earliest_arrival_time == -1:
        print(-1)
    else:
        print(earliest_arrival_time)

if __name__ == '__main__':
    main()

