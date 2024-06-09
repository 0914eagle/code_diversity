
def get_critical_cpus(n, m, k, blocks):
    critical_cpus = 0
    
    # Iterate over each block (layer)
    for block in blocks:
        # Iterate over each row (line) in the block
        for i in range(m):
            # Iterate over each column (character) in the row
            for j in range(k):
                # Check if the current CPU is working
                if block[i][j] == "1":
                    # Check if the current CPU controls any other CPUs
                    if controls_any_other_cpus(block, i, j, n, m, k):
                        critical_cpus += 1
    
    return critical_cpus

def controls_any_other_cpus(block, i, j, n, m, k):
    # Check if the current CPU controls any other CPUs in the same layer
    if i > 0 and block[i-1][j] == "1":
        return True
    if i < m-1 and block[i+1][j] == "1":
        return True
    if j > 0 and block[i][j-1] == "1":
        return True
    if j < k-1 and block[i][j+1] == "1":
        return True
    
    # Check if the current CPU controls any other CPUs in the same column
    for row in range(m):
        if row != i and block[row][j] == "1":
            return True
    
    # Check if the current CPU controls any other CPUs in the same row
    for col in range(k):
        if col != j and block[i][col] == "1":
            return True
    
    return False

