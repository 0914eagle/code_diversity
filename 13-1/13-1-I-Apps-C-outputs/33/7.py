
def is_possible(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if the sum of all elements is less than k
    if sum(a) < k:
        return "no"
    
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the median as the middle element
    median = a[n//2]
    
    # Loop through the array and check if the median is equal to k
    for i in range(n):
        if a[i] != median:
            return "no"
    
    return "yes"

