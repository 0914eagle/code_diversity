
def get_longest_log_length(logs, k):
    # Sort the logs in descending order
    logs.sort(reverse=True)
    
    # Initialize the longest log length and the number of cuts
    longest_log_length = 0
    num_cuts = 0
    
    # Iterate through the logs and calculate the longest log length after at most k cuts
    for log in logs:
        # If the number of cuts is greater than k, break the loop
        if num_cuts > k:
            break
        
        # Calculate the length of the longest log after the current log is cut
        longest_log_length = max(longest_log_length, log / 2)
        num_cuts += 1
    
    # Return the rounded up longest log length
    return int(math.ceil(longest_log_length))

def main():
    # Read the input data
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Calculate the longest log length after at most k cuts
    longest_log_length = get_longest_log_length(logs, k)
    
    # Print the result
    print(longest_log_length)

if __name__ == '__main__':
    main()

