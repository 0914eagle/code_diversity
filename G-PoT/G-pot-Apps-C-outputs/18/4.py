
# Read input
r, c = map(int, input().split())
start_bed, fridge = map(eval, input().split())
school_map = [input() for _ in range(r)]
p = int(input())
patrol_paths = [list(map(eval, input().split())) for _ in range(p)]

# Helper function to check if child can reach the fridge without being seen
def can_reach_fridge(turns):
    for path in patrol_paths:
        for i in range(turns):
            master_row, master_col = path[i % len(path)]
            if abs(master_row - fridge[0]) + abs(master_col - fridge[1]) <= turns - i:
                return False
    return True

# Binary search to find minimum turns
low, high = 0, r + c
while low < high:
    mid = (low + high) // 2
    if can_reach_fridge(mid):
        high = mid
    else:
        low = mid + 1

# Output result
if low == r + c:
    print("IMPOSSIBLE")
else:
    print(low)

