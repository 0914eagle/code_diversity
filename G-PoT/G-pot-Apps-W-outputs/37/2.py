
def possible_stop_heights(up_days, down_days):
    N = up_days + down_days + 1
    heights = []
    
    for i in range(1, up_days + 2):
        heights.append(i)
    
    for i in range(N, up_days + 1, -1):
        heights.append(i)
    
    return heights

# Input
up_days = int(input())
down_days = int(input())

# Output
result = possible_stop_heights(up_days, down_days)
print(*result)
