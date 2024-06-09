
def count_critical_cpus(n, m, k, blocks):
    # Initialize a dictionary to store the critical CPUs
    critical_cpus = {}

    # Iterate over each block (layer)
    for block in blocks:
        # Iterate over each row (line) in the block
        for i, row in enumerate(block):
            # Iterate over each column (character) in the row
            for j, char in enumerate(row):
                # If the current CPU is malfunctioning, skip it
                if char == "0":
                    continue
                # If the current CPU is not malfunctioning, check if it controls any other CPUs
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # If the controlled CPU is also malfunctioning, skip it
                        if blocks[x][y] == "0":
                            continue
                        # If the controlled CPU is not malfunctioning, add it to the critical CPUs dictionary
                        critical_cpus[(i, j)] = True

    # Return the number of critical CPUs
    return len(critical_cpus)

