
def get_order(ants1, ants2, T):
    # Initialize the order of the ants after T seconds
    order = ""
    
    # Loop through each second
    for second in range(T):
        # Loop through each ant in the first row
        for i in range(len(ants1)):
            # If the ant is not the first ant in the row
            if i > 0:
                # Get the ant in front of the current ant
                front_ant = ants1[i-1]
                
                # If the ant in front of the current ant is in the second row and is moving in the opposite direction
                if front_ant in ants2 and ants2.index(front_ant) < i:
                    # Swap the positions of the current ant and the ant in front of it
                    ants1[i-1], ants1[i] = ants1[i], ants1[i-1]
    
    # Add the ants in the first row to the order
    order += "".join(ants1)
    
    # Add the ants in the second row to the order
    order += "".join(ants2)
    
    return order

