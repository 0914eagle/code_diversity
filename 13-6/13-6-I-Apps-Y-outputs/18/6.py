
def solve(l1, r1, l2, r2):
    # Find the middle point of the first segment
    mid1 = (l1 + r1) // 2
    
    # Find the middle point of the second segment
    mid2 = (l2 + r2) // 2
    
    # If the middle points of the two segments are equal, return them
    if mid1 == mid2:
        return mid1, mid2
    
    # If the middle point of the first segment is to the left of the second segment, recurse on the left half of the first segment and the second segment
    elif mid1 < mid2:
        return solve(l1, mid1, l2, mid2)
    
    # If the middle point of the first segment is to the right of the second segment, recurse on the right half of the first segment and the second segment
    else:
        return solve(mid1, r1, mid2, r2)
    
def solve_queries(queries):
    result = []
    for query in queries:
        l1, r1, l2, r2 = query
        a, b = solve(l1, r1, l2, r2)
        result.append([a, b])
    return result

