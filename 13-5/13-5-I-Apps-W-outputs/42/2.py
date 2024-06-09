
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
                    if controls_any_cpu(block, i, j):
                        critical_cpus += 1
    
    return critical_cpus

def controls_any_cpu(block, i, j):
    # Check if the current CPU controls any other CPUs in the same row
    if controls_cpu_in_row(block, i, j):
        return True
    # Check if the current CPU controls any other CPUs in the same column
    if controls_cpu_in_column(block, i, j):
        return True
    # Check if the current CPU controls any other CPUs in the same block (layer)
    if controls_cpu_in_block(block, i, j):
        return True
    return False

def controls_cpu_in_row(block, i, j):
    # Check if the current CPU controls any other CPUs in the same row
    for k in range(k):
        if block[i][k] == "1" and k != j:
            return True
    return False

def controls_cpu_in_column(block, i, j):
    # Check if the current CPU controls any other CPUs in the same column
    for k in range(m):
        if block[k][j] == "1" and k != i:
            return True
    return False

def controls_cpu_in_block(block, i, j):
    # Check if the current CPU controls any other CPUs in the same block (layer)
    for k in range(m):
        for l in range(k):
            if block[k][l] == "1" and (k != i or l != j):
                return True
    return False

