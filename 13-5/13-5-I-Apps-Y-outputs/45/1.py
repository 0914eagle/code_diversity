
def get_max_area(W, H, x, y):
    # Calculate the area of the rectangle
    area = W * H
    
    # Calculate the area of the two parts
    part1_area = (W - x) * min(H, y)
    part2_area = x * min(H, y)
    
    # Find the maximum possible area
    max_area = max(part1_area, part2_area)
    
    # Check if there are multiple ways to cut the rectangle and achieve the maximum area
    if part1_area == part2_area:
        multiple_ways = 1
    else:
        multiple_ways = 0
    
    return max_area, multiple_ways

