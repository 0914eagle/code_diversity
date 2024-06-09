
def solve(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if it is possible to make all elements equal to k in one operation
    if len(set(a)) == 1:
        return "no"
    
    # Sort the array and find the median
    a.sort()
    median = a[len(a) // 2]
    
    # Check if the median is equal to k
    if median == k:
        return "yes"
    
    # Check if it is possible to make all elements equal to k by replacing the median with k
    if all(x == median for x in a):
        return "yes"
    
    # Check if it is possible to make all elements equal to k by replacing the elements less than the median with k
    if all(x >= median for x in a):
        return "yes"
    
    # Check if it is possible to make all elements equal to k by replacing the elements greater than the median with k
    if all(x <= median for x in a):
        return "yes"
    
    # If none of the above conditions are met, it is not possible to make all elements equal to k
    return "no"

