
def solve(L, x1, y1, x2, y2):
    # Calculate the length of the wall
    wall_length = abs(x1 - x2)
    
    # Calculate the width of the wall
    wall_width = abs(y1 - y2)
    
    # Calculate the area of the lawn
    lawn_area = L
    
    # Calculate the length of the chain needed to cover the lawn
    chain_length = wall_length * lawn_area / wall_width
    
    # Round the chain length to the nearest whole meter
    chain_length = round(chain_length)
    
    return chain_length

