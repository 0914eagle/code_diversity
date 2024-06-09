
def find_possible_stop_heights(up_days, down_days):
    N = up_days + down_days + 1
    heights = [0] * N
    current_height = 1

    for i in range(up_days):
        heights[i] = current_height
        current_height += 1

    for i in range(N-1, up_days-1, -1):
        if heights[i] == 0:
            heights[i] = current_height
            current_height += 1

    for i in range(N):
        if heights[i] == 0:
            heights[i] = current_height
            current_height += 1

    return heights[1:]

# Input
up_days = int(input())
down_days = int(input())

# Output
possible_heights = find_possible_stop_heights(up_days, down_days)
print(*possible_heights)
