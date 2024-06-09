
def fidget_cubes(v):
    # Calculate the minimum length and width of the box to hold V fidget cubes
    length = (v ** 0.5) + 1
    width = v // length
    
    # Calculate the cost of the box
    cost = length * width
    
    return cost

