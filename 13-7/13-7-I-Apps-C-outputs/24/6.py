
def solve(n, k, arr):
    # Check if all elements are already equal to k
    if all(elem == k for elem in arr):
        return "yes"
    
    # Check if the array contains only one element
    if len(arr) == 1:
        return "no"
    
    # Sort the array in ascending order
    arr.sort()
    
    # Find the median of the array
    median = arr[len(arr) // 2]
    
    # Check if the median is equal to k
    if median == k:
        return "yes"
    
    # Check if the median is greater than k
    if median > k:
        # Find the first index where the element is greater than k
        first_greater_index = next((i for i, x in enumerate(arr) if x > k), len(arr))
        # Check if the first greater element is the median
        if arr[first_greater_index] == median:
            return "yes"
        else:
            return "no"
    
    # Check if the median is less than k
    if median < k:
        # Find the first index where the element is less than k
        first_less_index = next((i for i, x in enumerate(arr) if x < k), len(arr))
        # Check if the first less element is the median
        if arr[first_less_index] == median:
            return "yes"
        else:
            return "no"


