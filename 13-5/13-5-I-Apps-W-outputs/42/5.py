
def count_critical_cpus(n, m, k, blocks):
    # Initialize a dictionary to store the critical CPUs
    critical_cpus = {}

    # Loop through each block (layer)
    for block in blocks:
        # Loop through each row (line) in the block
        for i, row in enumerate(block):
            # Loop through each column (character) in the row
            for j, col in enumerate(row):
                # If the current CPU is malfunctioning, skip it
                if col == "0":
                    continue
                # Get the coordinates of the current CPU
                x = i // m
                y = i % m
                z = j // k
                # Check if the current CPU controls any other CPUs
                if controls_other_cpus(n, m, k, blocks, x, y, z):
                    # If it does, mark it as critical
                    critical_cpus[(x, y, z)] = True

    # Return the number of critical CPUs
    return len(critical_cpus)

def controls_other_cpus(n, m, k, blocks, x, y, z):
    # Initialize a set to store the controlled CPUs
    controlled_cpus = set()

    # Loop through each block (layer)
    for block in blocks:
        # Loop through each row (line) in the block
        for i, row in enumerate(block):
            # Loop through each column (character) in the row
            for j, col in enumerate(row):
                # If the current CPU is malfunctioning, skip it
                if col == "0":
                    continue
                # Get the coordinates of the current CPU
                a = i // m
                b = i % m
                c = j // k
                # Check if the current CPU controls the CPU at position (x, y, z)
                if a == x and b == y and c == z:
                    # If it does, add it to the set of controlled CPUs
                    controlled_cpus.add((a, b, c))

    # Return True if the set of controlled CPUs is not empty, False otherwise
    return len(controlled_cpus) > 0

