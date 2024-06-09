
def count_scary_subarrays(arr):
    n = len(arr)
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize a variable to store the count of scary subarrays
    count = 0
    # Loop through each subarray of length 1 to n
    for i in range(n):
        for j in range(i, n):
            # Check if the leftmost element of the subarray is the median of the subarray
            if arr[i] == arr[(i+j)//2]:
                count += 1
    return count

