
def solve(n, m, io_list):
    # Initialize a dictionary to store the IOUs
    io_dict = {}
    for i in range(n):
        io_dict[i] = {}
    for i, j, c in io_list:
        # If the IOU is not already in the dictionary, add it
        if j not in io_dict[i]:
            io_dict[i][j] = c
        # If the IOU is already in the dictionary, update the amount
        else:
            io_dict[i][j] += c
    
    # While there are still IOUs to cancel
    while True:
        # Find the smallest IOU amount in the dictionary
        min_amount = float('inf')
        for i in range(n):
            for j in range(n):
                if i != j and i in io_dict and j in io_dict[i] and io_dict[i][j] < min_amount:
                    min_amount = io_dict[i][j]
        
        # If there are no more IOUs to cancel, break the loop
        if min_amount == float('inf'):
            break
        
        # Cancel the smallest IOU amount
        for i in range(n):
            for j in range(n):
                if i != j and i in io_dict and j in io_dict[i] and io_dict[i][j] == min_amount:
                    io_dict[i][j] = 0
                    if j in io_dict and i in io_dict[j] and io_dict[j][i] == min_amount:
                        io_dict[j][i] = 0
    
    # Count the number of IOUs left
    num_io_left = 0
    for i in range(n):
        for j in range(n):
            if i != j and i in io_dict and j in io_dict[i] and io_dict[i][j] > 0:
                num_io_left += 1
    
    # Return the number of IOUs left and the IOUs that are left
    return num_io_left, io_dict

