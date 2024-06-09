
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
                    # Check if the CPU above, below, and to the sides are working
                    if i > 0 and blocks[block][i-1][j] == "0":
                        critical_cpus += 1
                    if i < m-1 and blocks[block][i+1][j] == "0":
                        critical_cpus += 1
                    if j > 0 and blocks[block][i][j-1] == "0":
                        critical_cpus += 1
                    if j < k-1 and blocks[block][i][j+1] == "0":
                        critical_cpus += 1
    return critical_cpus

