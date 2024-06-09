
def solve(n, k):
    # Check if all elements are already equal to k
    if all(x == k for x in a):
        return "yes"
    
    # Check if it is possible to make all elements equal to k in one operation
    if len(set(a)) == 1:
        return "yes"
    
    # Check if it is possible to make all elements equal to k in two operations
    if len(set(a)) == 2 and a[0] == k and a[-1] == k:
        return "yes"
    
    # Check if it is possible to make all elements equal to k in three operations
    if len(set(a)) == 3 and a[0] == k and a[1] == k and a[-1] == k:
        return "yes"
    
    # If none of the above conditions are met, it is not possible to make all elements equal to k
    return "no"

