
def find_possible_stop_heights(up_days, down_days):
    n = up_days + down_days + 1
    heights = []

    for i in range(1, up_days + 2):
        heights.append(i)

    for i in range(n, up_days + 1, -1):
        heights.append(i)

    return heights

# Input
up_days = int(input())
down_days = int(input())

# Output
possible_heights = find_possible_stop_heights(up_days, down_days)
print(*possible_heights)
