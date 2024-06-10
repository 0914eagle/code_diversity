
def get_max_length(logs, k):
    # Sort the logs in descending order
    logs.sort(reverse=True)
    
    # Initialize the maximum length and the number of cuts
    max_length = 0
    num_cuts = 0
    
    # Loop through the logs and calculate the maximum length after at most k cuts
    for log in logs:
        # If the number of cuts is less than k, we can make at most one cut
        if num_cuts < k:
            max_length = max(max_length, log)
            num_cuts += 1
        # If the number of cuts is equal to k, we can no longer make any cuts
        else:
            break
    
    return max_length

def main():
    # Read the input from stdin
    n, k = map(int, input().split())
    logs = list(map(int, input().split()))
    
    # Get the maximum length after at most k cuts
    max_length = get_max_length(logs, k)
    
    # Print the result
    print(max_length)

if __name__ == '__main__':
    main()

