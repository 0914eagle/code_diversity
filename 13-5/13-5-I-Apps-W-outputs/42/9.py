
def count_critical_cpus(n, m, k, blocks):
    # Initialize a 3D array to represent the state of the CPUs
    cpu_state = [[[False] * k for _ in range(m)] for _ in range(n)]

    # Parse the blocks and set the state of the CPUs
    for i, block in enumerate(blocks):
        for j, line in enumerate(block.splitlines()):
            for k, char in enumerate(line):
                if char == "1":
                    cpu_state[i][j][k] = True

    # Initialize a set to store the critical CPUs
    critical_cpus = set()

    # Iterate over each CPU and check if it is critical
    for i in range(n):
        for j in range(m):
            for k in range(k):
                # If the CPU is working and has at least one neighbor that is not working, it is critical
                if cpu_state[i][j][k] and any(not cpu_state[x][y][z] for x in [i-1, i, i+1] for y in [j-1, j, j+1] for z in [k-1, k, k+1] if x in range(n) and y in range(m) and z in range(k)):
                    critical_cpus.add((i, j, k))

    return len(critical_cpus)

