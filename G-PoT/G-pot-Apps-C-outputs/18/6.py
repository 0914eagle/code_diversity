
# Read input
r, c = map(int, input().split())
start_bed, fridge = map(eval, input().split())
school_map = [input() for _ in range(r)]
p = int(input())
patrol_paths = [list(map(eval, input().split())) for _ in range(p)]

# Function to check if child can reach the fridge without being seen
def can_reach_fridge_in_time(turns):
    for i in range(1, turns+1):
        for master_path in patrol_paths:
            for j in range(len(master_path)):
                if j < i:
                    master_pos = master_path[j]
                    if abs(master_pos[0] - start_bed[0]) + abs(master_pos[1] - start_bed[1]) <= i:
                        return False
    return True

# Binary search to find minimum turns
low, high = 0, r*c
result = -1
while low <= high:
    mid = (low + high) // 2
    if can_reach_fridge_in_time(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1

# Output result
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)
