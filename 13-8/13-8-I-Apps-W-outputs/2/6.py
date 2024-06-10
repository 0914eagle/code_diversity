
def get_max_length(logs, K):
    # Sort the logs by length in descending order
    logs.sort(reverse=True)
    
    # Initialize the maximum length and the number of cuts
    max_length = 0
    num_cuts = 0
    
    # Loop through the logs and make cuts
    for log in logs:
        # Check if the number of cuts is less than or equal to K
        if num_cuts <= K:
            # Calculate the length of the longest log after the cut
            max_length = max(max_length, log // 2)
            # Increment the number of cuts
            num_cuts += 1
        else:
            # If the number of cuts is greater than K, break the loop
            break
    
    # Return the rounded up maximum length
    return int(math.ceil(max_length))

def main():
    # Read the input
    N, K = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Get the maximum length after at most K cuts
    max_length = get_max_length(logs, K)
    
    # Print the result
    print(max_length)

if __name__ == '__main__':
    main()

