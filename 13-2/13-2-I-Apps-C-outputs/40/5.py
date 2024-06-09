
def solve(n, m, t, op):
    # Initialize a 2D array to store the possible values for each cell
    values = [[[] for _ in range(n)] for _ in range(n)]
    
    # Fill in the values for the first cell
    values[0][0] = list(range(1, n+1))
    
    # Iterate over the remaining cells
    for i in range(1, m):
        for j in range(i):
            # If the cells are connected, copy the values from the previous cell
            if j % n == i % n:
                values[i][j] = values[j][j]
            # Otherwise, use the arithmetic operator to generate the possible values
            else:
                if op == "+":
                    values[i][j] = [x + y for x in values[j][j] for y in values[j][j]]
                elif op == "-":
                    values[i][j] = [x - y for x in values[j][j] for y in values[j][j]]
                elif op == "*":
                    values[i][j] = [x * y for x in values[j][j] for y in values[j][j]]
                elif op == "/":
                    values[i][j] = [x // y for x in values[j][j] for y in values[j][j] if y != 0]
    
    # Flatten the 2D array into a 1D array
    values = [item for sublist in values for item in sublist]
    
    # Count the number of valid ways to fill in the section
    count = 0
    for assignment in itertools.product(*values):
        if sum(assignment) == t:
            count += 1
    
    return count

