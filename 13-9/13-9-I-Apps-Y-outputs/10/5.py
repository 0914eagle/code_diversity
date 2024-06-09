
def solve(l1, r1, l2, r2):
    # Find the middle point of the first segment
    mid1 = (l1 + r1) // 2
    
    # Find the middle point of the second segment
    mid2 = (l2 + r2) // 2
    
    # If the middle points of the two segments are the same, return any point within the segments
    if mid1 == mid2:
        return l1, r2
    
    # If the middle points of the two segments are not the same, return the middle point of the first segment and the middle point of the second segment
    else:
        return mid1, mid2

