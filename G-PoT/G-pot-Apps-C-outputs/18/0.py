
# Read input
r, c = map(int, input().split())
start_bed, fridge = eval(input()), eval(input())
school_map = [input() for _ in range(r)]
p = int(input())
patrol_paths = [list(map(eval, input().split()[1:])) for _ in range(p)]

# Function to check if child can reach the fridge without being seen
def can_reach_fridge(turns):
    for master_path in patrol_paths:
        for i in range(len(master_path)):
            master_pos = master_path[i]
            if i + turns >= len(master_path):
                master_pos = master_path[-1 - (i + turns - len(master_path))]
            for j in range(r):
                if school_map[j][master_pos[1]] == '#' and start_bed[1] <= master_pos[1] <= fridge[1]:
                    return False
            for k in range(c):
                if school_map[master_pos[0]][k] == '#' and start_bed[0] <= master_pos[0] <= fridge[0]:
                    return False
    return True

# Binary search to find minimum number of turns
low, high = 0, 1000
while low < high:
    mid = (low + high) // 2
    if can_reach_fridge(mid):
        high = mid
    else:
        low = mid + 1

# Output result
if low == 1000:
    print("IMPOSSIBLE")
else:
    print(low)
