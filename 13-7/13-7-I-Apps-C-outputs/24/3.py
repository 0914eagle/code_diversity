
def solve(n, k, a):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if the sum of all elements is less than k
    if sum(a) < k:
        return "no"
    
    # Sort the array in non-decreasing order
    a.sort()
    
    # Initialize the median as the middle element
    median = a[n//2]
    
    # Loop through the array and replace each element with the median
    for i in range(n):
        a[i] = median
    
    # Check if all elements are now equal to k
    if all(x == k for x in a):
        return "yes"
    else:
        return "no"

