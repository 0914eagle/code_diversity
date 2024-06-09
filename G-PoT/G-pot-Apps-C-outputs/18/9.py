
# Read input
r, c = map(int, input().split())
start_bed, fridge = eval(input()), eval(input())
school_map = [input() for _ in range(r)]
p = int(input())
master_paths = [list(map(eval, input().split())) for _ in range(p)]

# Function to check if child can reach the fridge without being seen by masters
def can_reach_fridge(turns):
    for master_path in master_paths:
        for i in range(turns):
            master_pos = master_path[i % len(master_path)]
            if abs(master_pos[0] - start_bed[0]) + abs(master_pos[1] - start_bed[1]) <= turns - i:
                return False
    return True

# Binary search to find minimum number of turns for child to reach the fridge
low, high = 0, r + c
while low < high:
    mid = (low + high) // 2
    if can_reach_fridge(mid):
        high = mid
    else:
        low = mid + 1

# Output the result
if low == r + c:
    print("IMPOSSIBLE")
else:
    print(low)

