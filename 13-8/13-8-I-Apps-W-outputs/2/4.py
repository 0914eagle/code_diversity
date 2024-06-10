
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
        
        # If the number of cuts is less than k, calculate the maximum length after the current cut
        if num_cuts < k:
            # Calculate the length of the two logs after the current cut
            length1 = length / 2
            length2 = length - length1
            
            # Update the maximum length and the number of cuts
            max_length = max(max_length, length1, length2)
            num_cuts += 1
        else:
            # If the number of cuts is equal to k, update the maximum length
            max_length = max(max_length, length)
    
    # Return the rounded up maximum length
    return int(math.ceil(max_length))

def main():
    # Read the input
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Get the maximum length after at most k cuts
    max_length = get_max_length(logs, k)
    
    # Print the output
    print(max_length)

if __name__ == '__main__':
    main()

