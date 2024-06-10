
def get_earliest_arrival(n, m, t_a, t_b, k, a_list, b_list):
    # Sort the lists of departure times
    a_list.sort()
    b_list.sort()
    
    # Initialize the variables
    earliest_arrival = -1
    flights_cancelled = 0
    
    # Iterate through the flights from A to B
    for i in range(n):
        # Check if the flight from A to B is cancelled
        if flights_cancelled >= k:
            break
        
        # Get the departure time of the flight from A to B
        a_time = a_list[i]
        
        # Iterate through the flights from B to C
        for j in range(m):
            # Check if the flight from B to C is cancelled
            if flights_cancelled >= k:
                break
            
            # Get the departure time of the flight from B to C
            b_time = b_list[j]
            
            # Check if the flight from A to B and the flight from B to C can be connected
            if b_time >= a_time + t_a:
                # Calculate the arrival time at C
                arrival_time = b_time + t_b
                
                # Check if the arrival time at C is earlier than the current earliest arrival time
                if earliest_arrival == -1 or arrival_time < earliest_arrival:
                    earliest_arrival = arrival_time
                
                # Increment the number of flights cancelled
                flights_cancelled += 1
    
    return earliest_arrival

def main():
    # Read the input
    n, m, t_a, t_b, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    # Call the function to get the earliest arrival time
    earliest_arrival = get_earliest_arrival(n, m, t_a, t_b, k, a_list, b_list)
    
    # Print the result
    print(earliest_arrival)

if __name__ == '__main__':
    main()

