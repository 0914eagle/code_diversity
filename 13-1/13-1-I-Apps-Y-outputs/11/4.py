
def f1(N1, N2, row1, row2, T):
    # Initialize the order of ants after T seconds
    order = ""
    
    # Loop through each second
    for i in range(T):
        # Loop through each ant in the first row
        for j in range(N1):
            # If the ant is not the first ant in the first row
            if j > 0:
                # Get the ant in front of the current ant
                front_ant = row1[j-1]
                
                # If the ant in front of the current ant is in the second row and is moving in the opposite direction
                if front_ant in row2 and row2.index(front_ant) < row2.index(row1[j]):
                    # Swap the positions of the current ant and the ant in front of it
                    row1[j-1], row1[j] = row1[j], row1[j-1]
    
    # Add the order of ants in the first row to the order after T seconds
    order += "".join(row1)
    
    # Add the order of ants in the second row to the order after T seconds
    order += "".join(row2)
    
    return order

