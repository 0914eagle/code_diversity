
def solve(n, m, io_list):
    # Initialize a dictionary to store the IOUs
    io_dict = {}
    for i in range(n):
        io_dict[i] = {}
    for i, j, c in io_list:
        # If the IOU is not already in the dictionary, add it
        if j not in io_dict[i]:
            io_dict[i][j] = c
        # If the IOU is already in the dictionary, add the amount to the existing amount
        else:
            io_dict[i][j] += c
    
    # While there are still IOUs to be settled
    while True:
        # Find the smallest amount of IOU that is still outstanding
        min_amount = float('inf')
        for i in range(n):
            for j in range(n):
                if i != j and i in io_dict[j] and io_dict[j][i] < min_amount:
                    min_amount = io_dict[j][i]
        
        # If there are no more IOUs to be settled, break the loop
        if min_amount == float('inf'):
            break
        
        # Settle the IOUs by reducing the amount by the smallest amount
        for i in range(n):
            for j in range(n):
                if i != j and i in io_dict[j] and io_dict[j][i] > 0:
                    io_dict[j][i] -= min_amount
        
    # Count the number of IOUs that are still outstanding
    num_io_left = 0
    for i in range(n):
        for j in range(n):
            if i != j and i in io_dict[j] and io_dict[j][i] > 0:
                num_io_left += 1
    
    # Return the number of IOUs that are still outstanding and the IOUs that are left
    return num_io_left, io_dict

