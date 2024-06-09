
def fidget_cubes(V):
    # Calculate the minimum number of rows and columns needed to hold V fidget cubes
    rows = columns = int(V ** 0.5)
    if rows ** 2 != V:
        rows += 1
    # Calculate the cost of the box
    cost = rows * columns
    return cost

