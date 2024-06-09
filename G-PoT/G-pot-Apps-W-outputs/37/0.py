
def possible_stop_heights(up_days, down_days):
    n = up_days + down_days + 1
    heights = []
    
    for i in range(up_days + 1):
        heights.append(n - i)
    
    for i in range(1, down_days + 1):
        heights.insert(i, i)
    
    return heights

# Input
up_days = int(input())
down_days = int(input())

# Output
print(*possible_stop_heights(up_days, down_days))
