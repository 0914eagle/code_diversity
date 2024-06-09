
def solve(n, q, arr, queries):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each query and calculate the sum of elements with indices from l to r
    for l, r in queries:
        sum = 0
        for i in range(l-1, r):
            sum += arr[i]
        max_sum = max(max_sum, sum)
    return max_sum

