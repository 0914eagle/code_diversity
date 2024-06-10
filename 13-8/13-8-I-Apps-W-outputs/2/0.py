
def get_longest_log(logs, k):
    # Sort the logs by length in descending order
    logs.sort(reverse=True)
    
    # Initialize the longest log length and the number of cuts
    longest_log_length = 0
    num_cuts = 0
    
    # Loop through the logs and cut them if possible
    for log in logs:
        # Check if the log is longer than the longest log length
        if log > longest_log_length:
            # Update the longest log length
            longest_log_length = log
        
        # Check if the number of cuts is less than the allowed number of cuts
        if num_cuts < k:
            # Increment the number of cuts
            num_cuts += 1
        
        # Check if the log is evenly divisible by 2
        if log % 2 == 0:
            # Update the log length and the number of cuts
            log //= 2
            num_cuts += 1
    
    # Return the rounded up longest log length
    return int(math.ceil(longest_log_length))

def main():
    # Read the number of logs and the allowed number of cuts
    n, k = map(int, input().split())
    
    # Read the lengths of the logs
    logs = list(map(int, input().split()))
    
    # Get the longest log length after at most k cuts
    longest_log_length = get_longest_log(logs, k)
    
    # Print the result
    print(longest_log_length)

if __name__ == '__main__':
    main()

