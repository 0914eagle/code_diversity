
# Read input
r, c = map(int, input().split())
start, end = eval(input()), eval(input())
grid = [input() for _ in range(r)]
p = int(input())
masters = [list(map(eval, input().split()[1:])) for _ in range(p)]

# Function to check if child can reach the jelly
def can_reach_jelly(turns):
    for master in masters:
        for i in range(turns+1):
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                mr, mc = master[0] + dr*i, master[1] + dc*i
                if 0 <= mr < r and 0 <= mc < c and grid[mr][mc] == '.':
                    return False
    return True

# Binary search for minimum turns
low, high = 0, r*c
while low < high:
    mid = (low + high) // 2
    if can_reach_jelly(mid):
        high = mid
    else:
        low = mid + 1

if low == r*c:
    print("IMPOSSIBLE")
else:
    print(low)
