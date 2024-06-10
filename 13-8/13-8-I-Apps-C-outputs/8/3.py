
def get_longest_exploration_sequence(arr, D, M):
    # Initialize a dictionary to store the length of the longest exploration sequence for each index
    dp = {i: 1 for i in range(len(arr))}
    
    # Loop through the array and calculate the length of the longest exploration sequence for each index
    for i in range(len(arr)):
        for j in range(i+1, min(i+D+1, len(arr))):
            if abs(arr[i] - arr[j]) <= M:
                dp[j] = max(dp[j], dp[i] + 1)
    
    # Return the length of the longest exploration sequence
    return max(dp.values())

def main():
    # Read the input data
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Calculate the length of the longest exploration sequence
    longest_sequence = get_longest_exploration_sequence(arr, D, M)
    
    # Print the output
    print(longest_sequence)

if __name__ == '__main__':
    main()

