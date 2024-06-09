
def solve(N, L, drawers):
    # Initialize a list to store the items
    items = [0] * (N + 1)
    # Initialize a list to store the drawer status
    drawer_status = [0] * (L + 1)
    # Initialize a list to store the output
    output = []

    # Iterate through each item
    for i in range(1, N + 1):
        # Get the pair of drawers for the current item
        drawer1, drawer2 = drawers[i - 1]

        # Check if either of the drawers is empty
        if drawer_status[drawer1] == 0 or drawer_status[drawer2] == 0:
            # Store the item in the empty drawer
            if drawer_status[drawer1] == 0:
                items[i] = drawer1
                drawer_status[drawer1] = 1
            else:
                items[i] = drawer2
                drawer_status[drawer2] = 1

        # Check if the item can be moved to its other drawer
        else:
            # Iterate through the drawers until an empty one is found or the item is moved back to a previously seen drawer
            while True:
                # Check if the item can be moved to its other drawer
                if items[i] == drawer1:
                    if drawer_status[drawer2] == 0:
                        items[i] = drawer2
                        drawer_status[drawer2] = 1
                        break
                    else:
                        items[i] = drawer1
                else:
                    if drawer_status[drawer1] == 0:
                        items[i] = drawer1
                        drawer_status[drawer1] = 1
                        break
                    else:
                        items[i] = drawer2

        # Add the output for the current item
        if items[i] != 0:
            output.append("LADICA")
        else:
            output.append("SMECE")

    return output

