
def get_earliest_arrival_time(n, m, t_a, t_b, k, a_list, b_list):
    # Sort the lists of flight times
    a_list.sort()
    b_list.sort()
    
    # Initialize the earliest arrival time as infinity
    earliest_arrival_time = float('inf')
    
    # Loop through all possible combinations of flights to cancel
    for i in range(k + 1):
        # Get the number of flights to cancel from A to B
        num_cancel_a = i
        
        # Get the number of flights to cancel from B to C
        num_cancel_b = k - i
        
        # Check if it is possible to cancel the specified number of flights
        if num_cancel_a <= n and num_cancel_b <= m:
            # Cancel the specified number of flights
            cancel_a_list = a_list[:num_cancel_a]
            cancel_b_list = b_list[num_cancel_b:]
            
            # Get the latest departure time from A to B
            latest_depart_a = a_list[num_cancel_a - 1] if num_cancel_a > 0 else 0
            
            # Get the earliest arrival time at B
            earliest_arrival_b = latest_depart_a + t_a
            
            # Check if it is possible to arrive at B on time
            if earliest_arrival_b <= b_list[0]:
                # Get the latest departure time from B to C
                latest_depart_b = b_list[num_cancel_b] if num_cancel_b > 0 else 0
                
                # Get the earliest arrival time at C
                earliest_arrival_c = latest_depart_b + t_b
                
                # Update the earliest arrival time if necessary
                if earliest_arrival_c < earliest_arrival_time:
                    earliest_arrival_time = earliest_arrival_c
    
    # Return the earliest arrival time or -1 if it is not possible to reach C
    if earliest_arrival_time == float('inf'):
        return -1
    else:
        return earliest_arrival_time

def main():
    # Read the input
    n, m, t_a, t_b, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    # Call the function to get the earliest arrival time
    earliest_arrival_time = get_earliest_arrival_time(n, m, t_a, t_b, k, a_list, b_list)
    
    # Print the result
    print(earliest_arrival_time)

if __name__ == '__main__':
    main()

