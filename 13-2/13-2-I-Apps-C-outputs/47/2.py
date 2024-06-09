
def solve(n, m, io_list):
    # Initialize a dictionary to store the IOUs
    io_dict = {}
    for i in range(n):
        io_dict[i] = {}
    for i, j, c in io_list:
        if i not in io_dict[j]:
            io_dict[j][i] = -c
        else:
            io_dict[j][i] -= c
        if j not in io_dict[i]:
            io_dict[i][j] = c
        else:
            io_dict[i][j] += c
    
    # Find cycles and cancel IOUs
    while True:
        canceled = False
        for i in range(n):
            for j in range(i+1, n):
                if i in io_dict[j] and j in io_dict[i]:
                    canceled = True
                    io_dict[i][j] = 0
                    io_dict[j][i] = 0
        if not canceled:
            break
    
    # Count the number of IOUs left and output them
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if io_dict[i][j] != 0:
                count += 1
    print(count)
    for i in range(n):
        for j in range(i+1, n):
            if io_dict[i][j] != 0:
                print(i, j, io_dict[i][j])

