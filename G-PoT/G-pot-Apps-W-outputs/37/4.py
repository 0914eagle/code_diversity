
def find_possible_stop_heights(up_days, down_days):
    total_days = up_days + down_days + 1
    heights = list(range(1, total_days + 1))
    if up_days == 0:
        return heights[::-1]
    elif down_days == 0:
        return heights
    else:
        return heights[1:-1] + [heights[-1]] + [heights[0]]

# Input
up_days = int(input())
down_days = int(input())

# Output
possible_heights = find_possible_stop_heights(up_days, down_days)
print(*possible_heights)
