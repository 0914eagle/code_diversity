
def get_max_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be the sum of the first n elements
    max_sum = sum(arr[:len(arr)//2])
    # Iterate over the array and calculate the sum of the first n elements
    # after changing the sign of each element
    for i in range(len(arr)//2):
        max_sum = max(max_sum, sum(arr[:i+1]) + sum(arr[i+1:])*-1)
    return max_sum

