
def possible_stop_heights(up_days, down_days):
    n = up_days + down_days + 1
    heights = []
    
    for i in range(1, up_days + 1):
        heights.append(n - i)
    
    for i in range(1, down_days + 1):
        heights.append(i)
    
    heights.append(up_days + 1)
    
    return heights

# Example usage
up_days = 2
down_days = 1
print(*possible_stop_heights(up_days, down_days))
