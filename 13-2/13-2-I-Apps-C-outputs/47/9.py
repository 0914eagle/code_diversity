
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
    
    # While there are any IOUs left, find the smallest IOU and cancel it
    while any(io_dict[i] for i in range(n)):
        # Find the smallest IOU
        smallest_io = float('inf')
        for i in range(n):
            for j in io_dict[i]:
                if io_dict[i][j] < smallest_io:
                    smallest_io = io_dict[i][j]
                    a = i
                    b = j
        
        # Cancel the smallest IOU
        io_dict[a][b] -= smallest_io
        io_dict[b][a] -= smallest_io
    
    # Return the number of IOUs left and the IOUs that are left
    return len(io_dict[0]), [io for i in io_dict for io in io_dict[i].items() if io[1] > 0]

