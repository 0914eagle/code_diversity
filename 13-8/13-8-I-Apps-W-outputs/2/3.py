
def get_longest_log_length(logs, cuts):
    # Sort the logs in descending order
    logs.sort(reverse=True)
    
    # Initialize the longest log length and the current cuts
    longest_log_length = 0
    current_cuts = 0
    
    # Iterate through the logs and calculate the longest log length after each cut
    for log in logs:
        # If the current cuts are greater than or equal to the allowed cuts, break the loop
        if current_cuts >= cuts:
            break
        
        # Calculate the length of the longest log after the current cut
        longest_log_length = max(longest_log_length, log / 2)
        
        # Increment the current cuts
        current_cuts += 1
    
    # Return the longest log length after the allowed cuts
    return longest_log_length

def main():
    # Read the input data
    num_logs, cuts = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Find the longest log length after at most K cuts
    longest_log_length = get_longest_log_length(logs, cuts)
    
    # Print the result
    print(round(longest_log_length))

if __name__ == '__main__':
    main()

