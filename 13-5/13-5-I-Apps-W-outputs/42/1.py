
def get_critical_cpus(n, m, k, blocks):
    critical_cpus = 0
    
    # Iterate through each block
    for block in blocks:
        # Iterate through each row in the block
        for i in range(m):
            # Iterate through each column in the row
            for j in range(k):
                # Check if the current CPU is working
                if block[i][j] == "1":
                    # Check if the current CPU controls any other CPUs
                    if controls_any_other_cpus(n, m, k, blocks, i, j):
                        critical_cpus += 1
    
    return critical_cpus

def controls_any_other_cpus(n, m, k, blocks, i, j):
    # Check if the current CPU controls any other CPUs in the same layer
    if controls_any_other_cpus_in_same_layer(n, m, k, blocks, i, j):
        return True
    # Check if the current CPU controls any other CPUs in the next layer
    if controls_any_other_cpus_in_next_layer(n, m, k, blocks, i, j):
        return True
    # Check if the current CPU controls any other CPUs in the previous layer
    if controls_any_other_cpus_in_previous_layer(n, m, k, blocks, i, j):
        return True
    
    return False

def controls_any_other_cpus_in_same_layer(n, m, k, blocks, i, j):
    # Check if the current CPU controls any other CPUs in the same layer
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < m and y >= 0 and y < k and blocks[i][j] == "1" and blocks[x][y] == "1" and (x != i or y != j):
                return True
    return False

def controls_any_other_cpus_in_next_layer(n, m, k, blocks, i, j):
    # Check if the current CPU controls any other CPUs in the next layer
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < m and y >= 0 and y < k and blocks[i][j] == "1" and blocks[x+1][y] == "1" and (x != i or y != j):
                return True
    return False

def controls_any_other_cpus_in_previous_layer(n, m, k, blocks, i, j):
    # Check if the current CPU controls any other CPUs in the previous layer
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < m and y >= 0 and y < k and blocks[i][j] == "1" and blocks[x-1][y] == "1" and (x != i or y != j):
                return True
    return False

