
def max_sum_after_k_swap(arr, k):
    n = len(arr)
    # Sort the array to get the maximum sum
    arr.sort()
    # Initialize the maximum sum with the current sum
    max_sum = sum(arr)
    # Loop through the array and perform swap operations
    for i in range(n-1):
        for j in range(i+1, n):
            # Check if the number of swap operations is less than or equal to k
            if k > 0:
                # Perform the swap operation and calculate the sum
                arr[i], arr[j] = arr[j], arr[i]
                sum_after_swap = sum(arr)
                # Update the maximum sum if the current sum is greater
                if sum_after_swap > max_sum:
                    max_sum = sum_after_swap
                # Decrement the number of swap operations
                k -= 1
    return max_sum

