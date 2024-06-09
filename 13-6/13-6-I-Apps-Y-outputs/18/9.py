
def solve(l1, r1, l2, r2):
    # Find the smaller segment
    if r1 - l1 < r2 - l2:
        small_seg = [l1, r1]
        big_seg = [l2, r2]
    else:
        small_seg = [l2, r2]
        big_seg = [l1, r1]
    
    # Check if the small segment is inside the big segment
    if small_seg[0] >= big_seg[0] and small_seg[1] <= big_seg[1]:
        # If the small segment is inside the big segment, return any point from the big segment that is not in the small segment
        return [big_seg[0], big_seg[1] + 1]
    
    # If the small segment is not inside the big segment, return any point from the big segment that is not in the small segment
    return [big_seg[0], big_seg[1] + 1]

