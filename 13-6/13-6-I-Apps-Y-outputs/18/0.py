
def solve(l1, r1, l2, r2):
    # Find the leftmost and rightmost points of the two segments
    left = max(l1, l2)
    right = min(r1, r2)
    
    # If the segments do not overlap, return None
    if left >= right:
        return None
    
    # Find the middle point of the overlap
    mid = (left + right) // 2
    
    # Return the two points
    return (mid, mid + 1)

