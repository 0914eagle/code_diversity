
def read_input():
    N, K = map(int, input().split())
    logs = list(map(int, input().split()))
    return N, K, logs

def get_optimal_length(logs, K):
    # Sort the logs in non-decreasing order
    logs.sort()
    
    # Initialize the optimal length to be the longest log
    optimal_length = logs[-1]
    
    # Iterate through the logs and try to cut them
    for i in range(N-1):
        # Calculate the distance from the current log to the end of the list
        distance = logs[i] - optimal_length
        
        # If the distance is non-zero and the number of cuts is still available, try to cut the log
        if distance > 0 and K > 0:
            # Cut the log and update the optimal length
            optimal_length += distance
            K -= 1
    
    return optimal_length

def main():
    N, K, logs = read_input()
    optimal_length = get_optimal_length(logs, K)
    print(int(optimal_length))

if __name__ == '__main__':
    main()

