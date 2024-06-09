
def solve(a):
    # Check if all elements in the array are equal
    if len(set(a)) == 1:
        return "YES"
    
    # Sort the array in ascending order
    a.sort()
    
    # Initialize a variable to keep track of the minimum difference between elements
    min_diff = float("inf")
    
    # Iterate over the array and find the minimum difference between elements
    for i in range(len(a) - 1):
        diff = a[i+1] - a[i]
        if diff < min_diff:
            min_diff = diff
    
    # Check if the minimum difference is less than or equal to 1
    if min_diff <= 1:
        return "YES"
    else:
        return "NO"

