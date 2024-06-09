
def solve(l1, r1, l2, r2):
    # Find the set of all integers that are in both segments
    common_ints = set(range(l1, r1+1)).intersection(range(l2, r2+1))
    
    # Choose the first integer as the smallest integer in the common set
    a = min(common_ints)
    
    # Choose the second integer as the largest integer in the common set
    b = max(common_ints)
    
    return [a, b]

