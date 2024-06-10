
def get_max_length(logs, k):
    # Sort the logs in non-decreasing order
    logs.sort()
    
    # Initialize the maximum length and the number of cuts
    max_length = 0
    num_cuts = 0
    
    # Iterate through the logs and calculate the maximum length after at most k cuts
    for i in range(len(logs)):
        # Calculate the length of the current log
        length = logs[i]
        
        # Check if the current log can be cut
        if length > max_length and num_cuts < k:
            # Cut the current log in half and update the maximum length
            max_length = max(max_length, length // 2)
            num_cuts += 1
        else:
            # Update the maximum length with the current log
            max_length = max(max_length, length)
    
    # Return the rounded up maximum length
    return int(math.ceil(max_length))

def main():
    # Read the input
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Call the get_max_length function and print the result
    print(get_max_length(logs, k))

if __name__ == '__main__':
    main()

