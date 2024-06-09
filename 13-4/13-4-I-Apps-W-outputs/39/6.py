
def solve(n, q, arr, queries):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Iterate over the queries
    for l, r in queries:
        # Calculate the sum of elements in the query range
        sum = sum(arr[l-1:r])
        # Update the maximum sum
        max_sum = max(max_sum, sum)
    # Return the maximum sum
    return max_sum

