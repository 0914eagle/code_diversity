
def get_critical_cpus(n, m, k, blocks):
    critical_cpus = 0
    
    # Iterate over each block (layer)
    for block in blocks:
        # Iterate over each row (line) in the block
        for row in block:
            # Iterate over each column (character) in the row
            for col in range(k):
                # Check if the current CPU is working
                if row[col] == "1":
                    # Check if the CPU is controlling any other CPUs
                    if is_controlling_other_cpus(n, m, k, block, row, col):
                        critical_cpus += 1
    
    return critical_cpus

def is_controlling_other_cpus(n, m, k, block, row, col):
    # Check if the CPU is in the first or last row or column
    if row == 0 or row == m-1 or col == 0 or col == k-1:
        return False
    
    # Check if the CPU is controlling any other CPUs in the same block
    for i in range(k):
        if block[row-1][i] == "1" and block[row+1][i] == "1" and block[row][i-1] == "1" and block[row][i+1] == "1":
            return True
    
    # Check if the CPU is controlling any other CPUs in the adjacent blocks
    for i in range(n):
        for j in range(m):
            if i != row and j != col:
                if block[row][col] == "1" and block[i][j] == "1":
                    return True
    
    return False

