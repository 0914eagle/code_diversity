
def solve(l1, r1, l2, r2):
    # Find the largest integer that is less than or equal to the midpoint of the two segments
    mid = (l1 + r1 + l2 + r2) // 4
    
    # If the midpoint is within both segments, return it
    if l1 <= mid <= r1 and l2 <= mid <= r2:
        return mid
    
    # Otherwise, recursively call the function on the appropriate subintervals
    if mid < l1:
        return solve(l1, mid, l2, r2)
    else:
        return solve(l1, r1, l2, mid)

q = int(input())
for i in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    print(solve(l1, r1, l2, r2), solve(l1, r1, l2, r2))

