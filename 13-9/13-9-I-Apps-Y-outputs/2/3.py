
def fidget_cubes(V):
    # Calculate the minimum number of squares needed to hold V fidget cubes
    num_squares = (V // 6) + (1 if V % 6 > 0 else 0)
    
    # Calculate the cost of the box
    cost = num_squares * num_squares
    
    return cost

