
def solve(l1, r1, l2, r2):
    # Find the middle point of the first segment
    mid1 = (l1 + r1) // 2
    
    # Find the middle point of the second segment
    mid2 = (l2 + r2) // 2
    
    # If the middle points of the two segments are equal, return them
    if mid1 == mid2:
        return mid1, mid1
    
    # If the middle points of the two segments are not equal, return the smaller one
    # and the larger one
    if mid1 < mid2:
        return mid1, mid2
    else:
        return mid2, mid1

