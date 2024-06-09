
def solve(l1, r1, l2, r2):
    # Find the middle point of the first segment
    mid1 = (l1 + r1) // 2
    
    # Find the middle point of the second segment
    mid2 = (l2 + r2) // 2
    
    # If the middle points of the two segments are not equal, then we can choose them as the answer
    if mid1 != mid2:
        return [mid1, mid2]
    
    # If the middle points of the two segments are equal, then we need to recursively call the function to find the answer
    else:
        # If the first segment is longer than the second segment, then we can choose the middle point of the first segment and the right endpoint of the second segment as the answer
        if r1 - l1 > r2 - l2:
            return [mid1, r2]
        # If the first segment is shorter than the second segment, then we can choose the middle point of the first segment and the left endpoint of the second segment as the answer
        else:
            return [mid1, l2]

q = int(input())
for i in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    print(*solve(l1, r1, l2, r2))

