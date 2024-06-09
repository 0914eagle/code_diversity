
def solve(n, k, arr):
    # Check if all elements are already equal to k
    if all(elem == k for elem in arr):
        return "yes"
    
    # Check if it is possible to make all elements equal to k using the median operation
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                if arr[i] == k or arr[j] == k:
                    return "yes"
                else:
                    return "no"
    
    # If the array is already sorted, return "yes"
    if sorted(arr) == arr:
        return "yes"
    
    # If the array is not sorted and all elements are not equal to k, return "no"
    return "no"

