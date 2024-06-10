
def get_longest_exploration_sequence(arr, D, M):
    # Initialize a dictionary to store the length of the longest exploration sequence for each index
    dp = {i: 1 for i in range(len(arr))}
    
    # Loop through the array and calculate the length of the longest exploration sequence for each index
    for i in range(len(arr)):
        # Get the current element
        curr = arr[i]
        
        # Loop through the previous elements within the maximum jump distance D
        for j in range(i-D, i):
            # If the previous element is within the maximum jump distance and the difference in values is less than or equal to M, update the length of the longest exploration sequence for the current index
            if j >= 0 and abs(curr - arr[j]) <= M:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the length of the longest exploration sequence for the last index
    return dp[len(arr) - 1]

def main():
    # Read the input
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Calculate the length of the longest exploration sequence
    longest_sequence = get_longest_exploration_sequence(arr, D, M)
    
    # Print the result
    print(longest_sequence)

if __name__ == '__main__':
    main()

