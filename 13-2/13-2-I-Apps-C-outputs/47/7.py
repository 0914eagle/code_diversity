
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
    
    # While there are any IOUs left, find the smallest amount and cancel it out
    while any(io_dict[i] for i in range(n)):
        # Find the smallest amount owed by any friend
        smallest = min(io_dict[i][j] for i in range(n) for j in io_dict[i] if io_dict[i][j] > 0)
        # Find the friend who owes the smallest amount
        i = next((i for i in range(n) if smallest in io_dict[i] and io_dict[i][smallest] > 0), None)
        # Find the friend who is owed the smallest amount
        j = next(j for j in io_dict[i] if io_dict[i][j] == smallest)
        # Cancel out the IOU by updating the dictionary
        io_dict[i][j] -= smallest
        io_dict[j][i] += smallest
    
    # Return the number of IOUs left and the IOUs that are not canceled out
    return len(io_dict[i]), [(i, j, c) for i in range(n) for j in io_dict[i] if io_dict[i][j] > 0]

