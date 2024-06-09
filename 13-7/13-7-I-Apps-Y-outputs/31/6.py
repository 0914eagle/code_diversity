
def solve(arr):
    # Calculate the prefix sum of the array
    prefix_sum = [0]
    for i in range(len(arr)):
        prefix_sum.append(prefix_sum[i] + arr[i])
    
    # Initialize the minimum number of inserts to 0
    min_inserts = 0
    
    # Iterate through the prefix sum array
    for i in range(len(prefix_sum)):
        # Check if the prefix sum is 0
        if prefix_sum[i] == 0:
            # Calculate the number of inserts needed
            min_inserts += 1
        
        # Check if the prefix sum is negative
        if prefix_sum[i] < 0:
            # Calculate the number of inserts needed
            min_inserts += abs(prefix_sum[i])
    
    return min_inserts

