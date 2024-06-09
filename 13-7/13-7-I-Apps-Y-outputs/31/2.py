
def solve(arr):
    # Calculate the prefix sum of the array
    prefix_sum = [0]
    for i in range(len(arr)):
        prefix_sum.append(prefix_sum[i] + arr[i])
    
    # Initialize the minimum number of insertions to 0
    min_insertions = 0
    
    # Iterate through the prefix sum array
    for i in range(len(prefix_sum)):
        # If the prefix sum is 0, we need to insert an element to make it non-zero
        if prefix_sum[i] == 0:
            min_insertions += 1
    
    return min_insertions

