
def solve(n, m, t, op):
    # Initialize a 2D array to store the possible values for each cell
    values = [[[] for _ in range(n)] for _ in range(n)]
    
    # Fill in the values for the first cell
    for i in range(1, n+1):
        values[0][0].append(i)
    
    # Fill in the values for the remaining cells
    for i in range(1, m):
        for j in range(i):
            # Get the values for the previous cell
            prev_values = values[i-1][j]
            
            # Get the target value and operator for the current cell
            curr_target = t - prev_values[j]
            curr_op = op
            
            # Fill in the values for the current cell
            for k in range(1, n+1):
                if curr_op == '+':
                    if k >= curr_target:
                        values[i][j].append(k)
                elif curr_op == '-':
                    if k <= curr_target:
                        values[i][j].append(k)
                elif curr_op == '*':
                    if curr_target % k == 0:
                        values[i][j].append(k)
                elif curr_op == '/':
                    if curr_target * k == n:
                        values[i][j].append(k)
    
    # Count the number of valid ways to fill in the section
    count = 0
    for i in range(n):
        for j in range(n):
            if len(values[i][j]) > 0:
                count += 1
    
    return count

