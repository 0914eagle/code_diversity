
def get_critical_cpus(n, m, k, blocks):
    critical_cpus = 0
    
    # Iterate over each block (layer)
    for block in blocks:
        # Iterate over each row (line) in the block
        for row in block:
            # Iterate over each character (CPU) in the row
            for i, cpu in enumerate(row):
                # If the CPU is malfunctioning, skip it
                if cpu == "0":
                    continue
                # If the CPU is working, check if it controls any other CPUs
                for j in range(i+1, len(row)):
                    # If the CPU controls another CPU, increment the critical CPU count
                    if row[j] == "1":
                        critical_cpus += 1
    
    return critical_cpus

